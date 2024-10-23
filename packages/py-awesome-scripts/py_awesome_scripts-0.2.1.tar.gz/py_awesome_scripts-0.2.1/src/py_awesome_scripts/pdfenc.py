"""
功能: 加密当前路径下所有pdf文件。
命令: pdfenc -p [PASSWORD]
"""

import argparse
import concurrent.futures
import pathlib
import sys
import time
import typing

import pypdf


def enc_pdf(
    filepath: pathlib.Path, password: str
) -> typing.Tuple[pathlib.Path, typing.Optional[pathlib.Path]]:
    """加密单个pdf文件
    :param filepath: pdf文件路径
    :param password: 加密使用的密码
    :return 加密前, 后的文件路径
    """
    reader = pypdf.PdfReader(filepath)
    writer = pypdf.PdfWriter()

    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(
        user_password=password, owner_password=password, use_128bit=True
    )

    enc_pdf_file = filepath.with_suffix(".enc.pdf")
    try:
        with open(enc_pdf_file, "wb") as f:
            writer.write(f)
        return filepath, enc_pdf_file
    except IOError as e:
        print(f"[*] 写入加密文件[{enc_pdf_file.name}]失败, 错误信息: {e}")
        return filepath, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", dest="directory", type=str, default=".", help="pdf文件目录"
    )
    parser.add_argument("-p", dest="password", type=str, help="加密密码")

    args = parser.parse_args()
    directory, password = args.directory, args.password

    if not password:
        print("[!] 未指定密码, 退出...")
        parser.print_help(sys.stdout)
        return
    elif not pathlib.Path(directory).exists():
        print(f"[!] 输入参数不正确, 路径[{directory}]无效")
        parser.print_help(sys.stdout)
        return

    def is_encrypted(filepath: pathlib.Path) -> bool:
        """判断文件是否加密"""
        return pypdf.PdfReader(filepath).is_encrypted

    pdf_files = list(
        x for x in pathlib.Path(directory).rglob("*.pdf") if not is_encrypted(x)
    )
    print(f"[*] 找到待处理文件:{list(x.name for x in pdf_files)}")
    t0 = time.perf_counter()
    rets: typing.List[concurrent.futures.Future] = []
    print("[*] 启动线程")
    with concurrent.futures.ThreadPoolExecutor() as t:
        for pdf_file in pdf_files:
            print(f"[*] 开始处理[{pdf_file}]文件")
            rets.append(t.submit(enc_pdf, pdf_file, password))
    print("[*] 关闭线程")

    for future in concurrent.futures.as_completed(rets):
        old, new = future.result()
        print(f"[*] 加密pdf文件成功: {str(old)} => {str(new)}")
    print(
        f"[*] 处理数量=[{len(pdf_files)}], 用时=[{time.perf_counter() - t0:.3f}]s."
    )


if __name__ == "__main__":
    main()
