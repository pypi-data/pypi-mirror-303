import concurrent.futures
import datetime
from collections import namedtuple
from http import HTTPStatus
from pathlib import Path
from typing import Iterable

import requests

from ..config import CONFIG
from ..log import LOGGER
from .session import HEADERS

DownloadText = namedtuple("DownloadText", ["url", "dist", "text"])
DownloadRequest = namedtuple("DownloadRequest", ["url", "dist", "expire"])


class Downloader:
    def __init__(self, default_store_path=None) -> None:
        self.session = requests.Session()
        self.session.headers = HEADERS
        self.now = datetime.datetime.now()
        if default_store_path is not None:
            self.default_store_path = Path(default_store_path)
        else:
            self.default_store_path = Path("/tmp/clash")
        if not self.default_store_path.is_dir():
            self.default_store_path.mkdir(mode=755, parents=False, exist_ok=True)

    def down_one(self, url: str, dist: str, expire: datetime.timedelta):
        dist_path = Path(dist)
        if not dist_path.is_absolute():
            dist_path = self.default_store_path / dist_path
        if dist_path.is_file():
            lifetime = self.now - datetime.datetime.fromtimestamp(
                dist_path.stat().st_mtime
            )
            if lifetime <= expire:
                with open(dist_path, "r") as f:
                    return DownloadText(url, dist_path, f.read())
        LOGGER.debug(url)
        if dist.lower().endswith(".list") and CONFIG.proxy:
            response: requests.Response = self.session.get(
                url, proxies={"https": CONFIG.proxy}
            )
            LOGGER.info("使用代理下载完成 %s", url)
        else:
            try:
                response: requests.Response = self.session.get(url)
                LOGGER.info("直接下载完成 %s", url)
            except Exception:
                if CONFIG.proxy:
                    try:
                        response: requests.Response = self.session.get(
                            url, proxies={"https": CONFIG.proxy}
                        )
                        LOGGER.info("使用代理下载完成 %s", url)
                    except Exception:
                        LOGGER.error("使用代理下载失败 %s", url, exc_info=True)
                        return DownloadText(url, dist_path, None)
                else:
                    LOGGER.error("使用代理下载失败 %s", url, exc_info=True)
                    return DownloadText(url, dist_path, None)
        match response.status_code:
            case HTTPStatus.OK:
                text_res = response.text
            case _:
                LOGGER.error(
                    "下载 %s 失败，返回码：%d，返回字符：%s",
                    url,
                    response.status_code,
                    response.text,
                )
                return DownloadText(url, dist_path, None)
        with open(dist_path, "w") as f:
            f.write(text_res)
        return DownloadText(url, dist_path, text_res)

    def downloads(self, download_requests: Iterable[DownloadRequest]):
        res = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            # 提交任务到线程池
            futures = [
                executor.submit(
                    self.down_one,
                    download_request.url,
                    download_request.dist,
                    download_request.expire,
                )
                for download_request in download_requests
            ]

            # 等待所有任务完成
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    res.append(result)
                except Exception as error:
                    LOGGER.error("An error occurred", exc_info=True)
                    raise error
        return res
