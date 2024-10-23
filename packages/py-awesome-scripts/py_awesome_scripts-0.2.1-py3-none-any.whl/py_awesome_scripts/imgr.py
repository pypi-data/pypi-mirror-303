"""
功能: 将指定图像转为灰度图
命令: imgr [-b] [-w [width] ] [files]
"""

import argparse
import concurrent.futures
import os
import pathlib
import time

from PIL import Image


def convert_img(img_path: pathlib.Path, black_mode: bool, width: int):
    """转化图片

    :param img_path: 待处理图片路径
    :param black_mode: 黑白模式
    :param width: 缩放尺寸宽度
    """
    if not img_path.exists():
        raise FileNotFoundError(img_path)

    print(f"[*] 开始转换图片[{img_path.name}]")
    img = Image.open(img_path.as_posix())
    img_conv = img.convert("L")

    if black_mode:
        img_conv = img_conv.point(lambda x: 0 if x < 128 else 255, "1")

    if width:
        new_height = int(width / img_conv.width * img_conv.height)
        img_conv = img_conv.resize((width, new_height), resample=Image.LANCZOS)

    new_img_path = img_path.with_name(img_path.stem + "_conv.png")
    img_conv.save(new_img_path)
    print(f"[*] 转换图片[{img_path.name}]->[{new_img_path.name}]")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=str, help="待处理文件")
    parser.add_argument("-b", "--black", action="store_true", help="黑白模式")
    parser.add_argument(
        "-w", "--width", nargs="?", type=int, help="缩放尺寸宽度"
    )

    args = parser.parse_args()
    files: str = args.files
    black: bool = args.black
    width: int = args.width

    if not len(files):
        print("[*] 请输出待处理图片文件")
        parser.print_help()
        os.system("pause")
        return

    t0 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ret = list(
            executor.submit(convert_img, pathlib.Path(f), black, width)
            for f in files
        )
        for _ in concurrent.futures.as_completed(ret):
            pass
    print(f"[*] 处理结束, 总共用时: {time.perf_counter() - t0:.3f}s")


if __name__ == "__main__":
    main()
