"""
功能: 合并目录下所有 pdf 文件。最多包含两层目录，如果存在多层文件夹，则统一纳入根目录。
命令: pdfmerge -d [DIRECTORY]
"""

import argparse
import concurrent.futures
import dataclasses
import functools
import pathlib
import time
import typing

import pypdf

# 跳过的文件名或者文件夹名
IGNORED_FOLDERS = [".git", "__pycache__"]

# 合并后的文件名前缀
MERGE_MARK = "合并#"
# 最大搜索深度
MAX_SEARCH_DEPTH = 2


@dataclasses.dataclass
class PdfFileInfo:
    prefix: str
    files: typing.List[pathlib.Path]
    children: typing.List["PdfFileInfo"]

    def count(self) -> int:
        return len(self.files) + sum([x.count() for x in self.children])

    def __str__(self):
        fs = list(x.name for x in self.files)
        return f"prefix={self.prefix}, files={fs}, children={self.children}"

    def __repr__(self):
        return self.__str__()


def is_encrypted(filepath: pathlib.Path) -> bool:
    """判断pdf文件是否已经加密"""
    return pypdf.PdfReader(filepath).is_encrypted


def relative_depth(search_dir: pathlib.Path, root_dir: pathlib.Path) -> int:
    """搜索文件夹相对根文件夹深度"""
    try:
        relative_path = search_dir.relative_to(root_dir)
        return len(relative_path.parts)
    except ValueError:
        return 0


@functools.lru_cache(maxsize=128)
def search_directory(
    search_dir: pathlib.Path, root_dir: pathlib.Path
) -> PdfFileInfo:
    """搜索目录下的所有pdf文件"""
    if relative_depth(search_dir, root_dir) > MAX_SEARCH_DEPTH:
        return None

    children: typing.List[PdfFileInfo] = []
    folders = [
        d
        for d in sorted(search_dir.iterdir())
        if d.is_dir() and d.name not in IGNORED_FOLDERS
    ]
    for folder in folders:
        pdf_info = search_directory(folder, root_dir)
        if pdf_info is not None:
            children.append(pdf_info)

    pdf_files = list(
        x
        for x in sorted(search_dir.glob("*.pdf"))
        if not is_encrypted(x) and MERGE_MARK not in x.stem
    )
    if not len(pdf_files) and not len(children):
        return None

    prefix = search_dir.relative_to(root_dir).name
    return PdfFileInfo(prefix=prefix, files=pdf_files, children=children)


def merge_file_info(
    info: PdfFileInfo, root_dir: pathlib.Path, writer: pypdf.PdfWriter
):
    """按照 PdfFileInfo 进行合并"""
    page_num = 0
    if info.prefix:
        root_bookmark = writer.add_outline_item(info.prefix, 0)
    else:
        root_bookmark = None

    for pdf_filepath in info.files:
        with open(pdf_filepath.as_posix(), "rb") as pdf_file:
            reader = pypdf.PdfReader(pdf_file)
            writer.append(pdf_filepath.as_posix(), import_outline=False)
            writer.add_outline_item(
                pdf_filepath.stem, page_num, parent=root_bookmark
            )
            page_num += len(reader.pages)

    for child_info in info.children:
        merge_file_info(child_info, root_dir, writer=writer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        dest="directory",
        type=str,
        default=".",
        help="pdf文件目录",
    )

    args = parser.parse_args()
    directory = args.directory
    if not pathlib.Path(directory).exists():
        print(f"[*] 输入参数不正确，路径[{directory}]不存在")
        parser.print_help()
        return

    pdf_dir = (
        pathlib.Path(directory) if directory != "." else pathlib.Path.cwd()
    )
    pdf_info = search_directory(pdf_dir, pdf_dir)
    pdf_count = pdf_info.count() if pdf_info is not None else 0
    if pdf_count <= 1:
        print("[*] 未发现待合并文件, 退出...")
        return

    print(f"[*] 分析合并文件[{pdf_info}]\n[*] 总数[{pdf_count}]")
    t0 = time.perf_counter()
    print("[*] 启用线程池")
    writer = pypdf.PdfWriter()
    with concurrent.futures.ThreadPoolExecutor() as t:
        ret = t.submit(merge_file_info, pdf_info, pdf_dir, writer)
        if concurrent.futures.as_completed(ret):
            print(f"[*] 处理文件[{pdf_info}]结束")
        t.shutdown()
    target_filepath = pdf_dir / f"{MERGE_MARK}{pdf_dir.stem}.pdf"
    with open(target_filepath, "wb") as pdf_file:
        writer.write(pdf_file)
        writer.close()
    print(f"[*] 写入到文件[{target_filepath.name}]")
    print("[*] 关闭线程池")
    print(
        f"[*] 合并所有文件完成, 输出=[{target_filepath.name}], 用时=[{time.perf_counter() - t0:.3f}s]"
    )


if __name__ == "__main__":
    main()
