"""
功能：爬取网页中存在的链接地址
用法：scraplinks -d [url]
"""

import argparse
import concurrent.futures
import pathlib
import time
import typing
from urllib.parse import urlparse, ParseResult

import requests as rq
from bs4 import BeautifulSoup


def parse_url(url: str) -> typing.List[str]:
    parse: ParseResult = urlparse(url)

    if "http" not in parse.scheme:
        data = rq.get(f"https://{url}")
    else:
        data = rq.get(url)

    soup = BeautifulSoup(data.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href_text: str = link.get("href")
        if href_text.startswith("#"):
            href_text = f"{url}{href_text}"
        elif href_text.startswith("//"):
            href_text = f"https:{href_text}"
        elif href_text.startswith("/"):
            href_text = f"https://{parse.netloc}{href_text}"
        links.append(f"text={link.text}, url={href_text}")

    return links


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", dest="urls", nargs="+", type=str, help="目标 url 地址"
    )

    args = parser.parse_args()
    t0 = time.perf_counter()
    rets: typing.List[concurrent.futures.Future] = []
    if len(urls := args.urls):
        print("[*] 启动线程...")
        with concurrent.futures.ThreadPoolExecutor() as e:
            for url in urls:
                print(f"[*] 开始处理{url=}")
                rets.append(e.submit(parse_url, url))
        print("[*] 关闭线程...")

    with open(
        str(pathlib.Path.cwd() / "my_links.txt"), "w", encoding="utf-8"
    ) as f:
        for future in concurrent.futures.as_completed(rets):
            links: typing.List[str] = future.result()
            f.writelines("\n".join(links))
    print(f"[*] 目标数=[{len(urls)}]\n用时=[{time.perf_counter() - t0:.3f}]s.")


if __name__ == "__main__":
    main()
