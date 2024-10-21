import threading
import time
from .fd_utils import spin
from typing import Dict, Union, Any
import os
import httpx
from httpx import Client, Timeout
import json
import logging


package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
resource_path = os.path.join(package_path, "resources")
config_path = os.path.join(resource_path, "fd_python_config.json")
class FDHttpClient(spin):
    """
        HTTP客户端类，用于发送HTTP请求并返回JSON形式的响应
    """
    def __init__(
            self,
            # max_retries: int,
            # connetc_timeout: float,
    ):

        with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        self.max_retries = config["http_client"]["max_retries"]
        self.connect_timeout = config["http_client"]["connect_timeout"]
        self.read_timeout = config["http_client"]["read_timeout"]
        self.write_timeout = config["http_client"]["write_timeout"]
        self.pool_timeout = config["http_client"]["pool_timeout"]
        self.session = Client(timeout=Timeout(connect=self.connect_timeout,read=self.read_timeout,write=self.write_timeout,pool=self.pool_timeout),)

    def send_request(self, url: str, json_data: dict, method: str = "POST") -> dict:
        """发送请求并返回JSON形式的响应"""
        self.start_spinner()
        response = self.session.request(method=method, url=url, json=json_data)
        self.stop_spinner
        if response.status_code >= 500:
            # 如果服务器内部错误，则重试
            return self._retry_request(url, response.status_code, json_data, method)
        return response.json()

    def _retry_request(self, url: str, status_code: int, json_data: dict, method: str) -> dict:
        """重试发送请求"""
        retries = self.max_retries
        self.start_spinner()
        while retries > 0:
            retries -= 1
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    json=json_data,
                    timeout=self.connect_timeout,
                )
                if response.status_code < 500:
                    return response.json()
            except httpx.ReadTimeout:
                # 如果请求超时，则重试
                logging.warning("Request timed out, retrying...")
                continue
            except httpx.ConnectTimeout:
                # 如果连接超时，则重试
                logging.warning("Connection timed out, retrying...")
                continue
            except httpx.ConnectError:
                # 如果发生网络连接错误，则重试
                logging.warning("Network connection error, retrying...")
                continue
            except httpx.HTTPStatusError:
                # 如果服务器返回了非200状态码，则重试
                logging.warning(f"Server returned status code {response.status_code}, retrying...")
                continue
            except httpx.RequestError:
                # 如果请求过程中发生其他错误，则重试
                logging.warning("An error occurred during the request, retrying...")
                continue
            except Exception as e:
                # 捕获其他异常并重试
                logging.warning(f"An unexpected error occurred: {e}")
                continue
        self.stop_spinner()
        # 如果重试次数耗尽，则抛出异常
        raise httpx.RequestError("无法连接服务端")

    def send_request_fromdata(self, url: str, data: Dict[str, Union[str, bytes]], files: Dict[str, Any] = None, method: str = "POST") -> dict:
        """发送请求并返回JSON形式的响应，支持文件上传"""
        self.start_spinner()
        response = self.session.request(method=method, url=url, data=data, files=files)
        self.stop_spinner()
        if response.status_code >= 500:
            # 如果服务器内部错误，则重试
            return self._retry_request_fromdata(url,  data, files, method)
        return response.json()

    def _retry_request_fromdata(self, url: str,  data: Dict[str, Union[str, bytes]], files: Dict[str, Any], method: str) -> dict:
        """重试发送请求，支持文件上传"""
        retries = self.max_retries
        while retries > 0:
            retries -= 1
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    data=data,
                    files=files,
                    timeout=self.connect_timeout,
                )
                if response.status_code < 500:
                    return response.json()
            except httpx.ReadTimeout:
                logging.warning("Request timed out, retrying...")
                continue
            except httpx.ConnectTimeout:
                logging.warning("Connection timed out, retrying...")
                continue
            except httpx.ConnectionError:
                logging.warning("Network connection error, retrying...")
                continue
            except httpx.HTTPStatusError:
                logging.warning(f"Server returned status code {response.status_code}, retrying...")
                continue
            except httpx.RequestError:
                logging.warning("An error occurred during the request, retrying...")
                continue
            except Exception as e:
                logging.warning(f"An unexpected error occurred: {e}")
                continue

        raise httpx.RequestError("无法连接服务端")

    def close(self):
        """关闭会话"""
        self.session.close()

