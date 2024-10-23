"""
功能: 将当前路径下所有图片合并为pdf文件。
命令: img2pdf -d [DIRECTORY]
"""

import argparse
import pathlib
import time

from PIL import Image


def is_image_file(file_path: pathlib.Path) -> bool:
    """验证文件是否为图片

    Args:
        file_path (pathlib.Path): 文件路径

    Returns:
        bool: 是否为图片
    """
    try:
        with Image.open(file_path) as img:
            img.verify()  # 验证图像是否损坏
        return True
    except IOError:
        return False


def merge_images_to_pdf(
    input_dir: pathlib.Path, output_pdf: pathlib.Path
) -> None:
    """合并所有图片为pdf

    Args:
        input_dir (pathlib.Path): 输入路径
        output_pdf (pathlib.Path): 输出文件
    """
    t0 = time.perf_counter()
    images = list(sorted(f for f in input_dir.iterdir() if is_image_file(f)))

    if not images:
        print(f"[*] 路径[{input_dir}]下未找到图片文件.")
        return

    images_converted = []
    for image_file in images:
        img = Image.open(image_file)

        # 将图像转换为RGB格式，因为PDF支持RGB而非P模式（带透明度）
        img = img.convert("RGB")
        images_converted.append(img)

    # 保存第一个图像为PDF，并附加剩余的图像
    if images_converted:
        images_converted[0].save(
            output_pdf,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=images_converted[1:],
        )
        print(f"[*] 创建PDF文件[{output_pdf.name}]成功!")
        print(
            f"[*] 处理图片[{len(images)}]张, 用时[{time.perf_counter() - t0:.3f}]s."
        )
    else:
        print(f"[*] 路径[{input_dir}]下未找到图片文件.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        dest="directory",
        type=str,
        default=str(pathlib.Path.cwd()),
        help="pdf文件目录",
    )

    args = parser.parse_args()
    directory = args.directory

    if not pathlib.Path(directory).exists():
        print(f"[*] 输入参数不正确，路径[{directory}]不存在")
        parser.print_help()
        return

    input_dir = pathlib.Path(directory)
    output_pdf = input_dir / f"{input_dir.name}.pdf"
    merge_images_to_pdf(input_dir, output_pdf)


if __name__ == "__main__":
    main()
