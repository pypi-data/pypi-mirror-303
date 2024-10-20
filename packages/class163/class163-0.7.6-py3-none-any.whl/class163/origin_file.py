"""
class163/orifin_file.py
Version: 0.6.7
Author: CooooldWind_/ChatGPT
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""
import threading
import requests
from requests.adapters import HTTPAdapter

class OriginFile(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.session = requests.Session()
        self.session.mount("http://", HTTPAdapter(max_retries=3))
        self.session.mount("https://", HTTPAdapter(max_retries=3))
        self.tot_size = 0
        self.now_size = 0
        self.data = bytes()
        self.percentage = 0.0
        self.lock = threading.Lock()
        self._fetch_file_size()

    def _fetch_file_size(self):
        try:
            head = self.session.head(self.url, allow_redirects=True)
            self.url = head.url  # 如果有重定向，更新 URL
            self.tot_size = int(head.headers.get('Content-Length', 0))
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"获取文件大小时出错: {e}")
        except KeyError:
            raise RuntimeError("获取文件大小时发生错误：未找到 'Content-Length' 标头")

    def begin_download(self, multi_thread: bool = False):
        if multi_thread:
            super().start()  # 启动线程
        else:
            self.run()  # 直接调用 run 方法

    def run(self):
        try:
            with self.session.get(self.url, stream=True) as response:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        with self.lock:
                            self.data += chunk
                            self.now_size += len(chunk)
                            if self.tot_size > 0:
                                self.percentage = (self.now_size / self.tot_size) * 100
        except requests.exceptions.HTTPError as e:
            self.handle_http_error(e.response.status_code)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"下载文件时出错: {e}")

    def handle_http_error(self, status_code):
        error_messages = {
            400: "错误请求：服务器无法理解请求。",
            401: "未授权：请求需要用户验证。",
            403: "禁止访问：服务器拒绝请求。",
            404: "未找到：服务器找不到请求的资源。",
            500: "服务器内部错误：服务器遇到错误，无法完成请求。",
            502: "错误网关：服务器作为网关或代理，从上游服务器收到无效响应。",
            503: "服务不可用：服务器目前无法使用（过载或维护）。",
            504: "网关超时：服务器作为网关或代理，未及时从上游服务器接收请求。"
        }
        message = error_messages.get(status_code, f"HTTP 错误：{status_code}")
        raise RuntimeError(message)

    def get_data(self) -> bytes:
        with self.lock:
            return self.data

    def get_percentage(self):
        with self.lock:
            return round(self.percentage, 3)