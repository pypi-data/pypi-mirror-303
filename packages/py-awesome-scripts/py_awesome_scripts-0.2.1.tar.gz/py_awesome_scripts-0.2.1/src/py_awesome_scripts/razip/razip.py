"""
功能: 对 RetroArch ROMS 进行压缩处理
命令: razip.exe
"""

import concurrent.futures
import pathlib
import time
import typing
import zipfile

DIR_SRC = pathlib.Path(__file__).parent
DIR_ROMS = DIR_SRC.parent.parent / "roms" / "FC"

ALLOWED_EXTENSIONS = (
    ".nes",
    ".fds",
    ".unf",
)


def process_file(zip_file_path: pathlib.Path) -> typing.Tuple[bool, str]:
    zf = zipfile.ZipFile(zip_file_path.as_posix(), "r", zipfile.ZIP_DEFLATED)
    nes_file_name, nes_file_path = None, None
    for file_info in zf.infolist():
        try:
            filename = file_info.filename.encode("cp437").decode("gbk")
            if pathlib.Path(filename).suffix.lower() in ALLOWED_EXTENSIONS:
                fn = pathlib.Path(filename.split("/")[-1])
                nes_file_name = fn.with_suffix(fn.suffix.lower()).name
                file_info.filename = nes_file_name
                nes_file_path = zip_file_path.parent / "temp" / nes_file_name
                zf.extract(
                    file_info, (zip_file_path.parent / "temp").as_posix()
                )
        except UnicodeDecodeError as e:
            return (
                False,
                f"[*] {file_info.filename}编码问题, {e}, {zip_file_path=}",
            )
    zf.close()

    if not nes_file_name or not nes_file_path:
        return False, f"[*] {zip_file_path.name}中不存在nes文件"

    new_zip_file = (
        zip_file_path.parent
        / "save"
        / (zip_file_path.stem + "##" + zip_file_path.suffix)
    )
    zf2 = zipfile.ZipFile(new_zip_file.as_posix(), "w", zipfile.ZIP_DEFLATED)
    zf2.write(nes_file_path, nes_file_name)
    zf2.close()
    return True, new_zip_file.name


if __name__ == "__main__":
    zip_files = [f for f in DIR_ROMS.glob("*.zip")]
    t0 = time.perf_counter()
    fs: typing.List[concurrent.futures.Future] = []
    with concurrent.futures.ThreadPoolExecutor() as t:
        for zip_file in zip_files:
            fs.append(t.submit(process_file, zip_file))

    with open(str(DIR_ROMS / "_error.log"), "w", encoding="utf8") as f:
        for future in concurrent.futures.as_completed(fs):
            result, content = future.result()
            if result:
                print(f"[*] 重命名文件成功: {content}")
            else:
                f.write(content + "\n")
    print(f"[*] 目标数=[{len(fs)}]\n用时=[{time.perf_counter() - t0:.3f}]s.")
