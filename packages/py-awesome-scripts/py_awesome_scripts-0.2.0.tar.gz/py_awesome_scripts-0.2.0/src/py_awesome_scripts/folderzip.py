"""
功能: 压缩目录下的所有文件/文件夹, 默认为当前目录
命令: folderzip.exe [DIRECTORIES ...]
特性: 使用内置压缩工具
"""

import argparse
import concurrent.futures
import pathlib
import shutil
import time
import typing

IGNORE_DIRS = [".git", ".idea", ".vscode", "__pycache__"]
IGNORE_FILES = [".gitignore"]
IGNORE = [*IGNORE_DIRS, *IGNORE_FILES]
IGNORE_EXT = [".zip", ".rar", ".7z", ".tar", ".gz"]


def zip_folder(folder: pathlib.Path) -> None:
    entries = list(
        f
        for f in folder.iterdir()
        if (f.is_dir() and f.stem not in IGNORE_DIRS)
    )
    for entry in entries:
        shutil.make_archive(entry, "zip", entry)
        print(f"[*] 压缩{'目录'}[{entry.name}]")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirs", nargs="?", type=str, help="待处理目录")

    args = parser.parse_args()
    dirs: typing.List[str] = args.dirs

    if dirs is None:
        targets = [pathlib.Path().cwd()]
    elif isinstance(dirs, str):
        targets = [pathlib.Path(dirs)]
    else:
        targets = [pathlib.Path(x) for x in dirs if pathlib.Path(x).exists()]

    t0 = time.perf_counter()
    print("[*] 启动线程")
    with concurrent.futures.ThreadPoolExecutor() as t:
        rets = [t.submit(zip_folder, d) for d in targets]
        for _ in concurrent.futures.as_completed(rets):
            pass
    print(f"[*] 处理结束, 用时: {time.perf_counter() - t0:.3f}s")


if __name__ == "__main__":
    main()
