"""
功能: 拆分指定 pdf 文件为多个 pdf
命令: pdfsplit -f [FILE] -r [RANGE] -o [OUT_DIR]
"""

import argparse
import pathlib
import time
import typing

import pypdf


def parse_split_range(
    rng: str, filepath: str = ""
) -> typing.List[typing.Tuple[int, int]]:
    """分析分割参数
    >>> parse_split_range('1,3,5')
    [(1, 1), (3, 3), (5, 5)]
    >>> parse_split_range('1, 3, 5')
    [(1, 1), (3, 3), (5, 5)]
    >>> parse_split_range('1-3')
    [(1, 3)]
    >>> parse_split_range('1, 3-4, 5')
    [(1, 1), (3, 4), (5, 5)]
    >>> parse_split_range('1-3,2,5')
    [(1, 3), (2, 2), (5, 5)]
    """
    if rng is None:
        with open(filepath, "rb") as f:
            reader = pypdf.PdfReader(f)
            return [(x + 1, x + 1) for x in range(len(reader.pages))]

    range_list = list(x.strip() for x in rng.split(","))
    items = []
    for e in range_list:
        if "-" in e:
            start, end = e.split("-")
            items.append((int(start), int(end)))
        else:
            items.append((int(e), int(e)))
    return items


def split_pdf_file_by_range(
    filepath: pathlib.Path,
    out_dir: pathlib.Path,
    pdf_ranges: typing.List[typing.Tuple[int, int]],
):
    """按照范围进行分割"""
    print(f"[*] 开始分割文件{filepath}")
    with open(filepath, "rb") as pdf_file:
        reader = pypdf.PdfReader(pdf_file)
        print(pdf_ranges)
        out_pdfs: typing.List[pathlib.Path] = list(
            out_dir / f"{filepath.stem}#{b}-{e}{filepath.suffix}"
            for (b, e) in pdf_ranges
        )
        for out_pdf, (start, end) in zip(out_pdfs, pdf_ranges):
            writer = pypdf.PdfWriter()

            for page_num in range(start - 1, end):
                if page_num < len(reader.pages):
                    writer.add_page(reader.pages[page_num])

            try:
                with open(out_pdf, "wb") as fw:
                    writer.write(fw)
            except OSError as e:
                print(f"[*] 写入文件[{out_pdf.name}]失败, 错误信息[{e}]")
            else:
                print(f"[*] 写入文件[{out_pdf.name}]成功")
            writer.close()
        reader.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", dest="file", type=str, help="待处理文件"
    )
    parser.add_argument(
        "-o",
        "--out_dir",
        dest="out_dir",
        type=str,
        default=".",
        help="输出目录",
    )
    parser.add_argument(
        "-r",
        "--range",
        dest="range",
        type=str,
        help="按范围分割, 如: 1-3,4-5",
    )

    args = parser.parse_args()
    file: str = args.file
    out_dir: str = args.out_dir
    rng: str = args.range

    split_range = parse_split_range(rng, filepath=file)
    print(f"[*] 待处理文件[{file}]")
    t0 = time.perf_counter()
    split_pdf_file_by_range(
        pathlib.Path(file),
        pathlib.Path(out_dir),
        split_range,
    )
    print(f"[*] 结束, 用时{time.perf_counter() - t0:.3f}s")


if __name__ == "__main__":
    main()
