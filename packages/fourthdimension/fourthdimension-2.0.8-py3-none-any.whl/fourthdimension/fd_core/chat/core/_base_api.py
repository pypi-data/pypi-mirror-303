from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._client import FourthDimensionAI


class BaseAPI:
    _client: FourthDimensionAI

    def __init__(self, client: FourthDimensionAI) -> None:
        self._client = client
        self._delete = client.delete
        self._get = client.get
        self._post = client.post
        self._put = client.put
        self._patch = client.patch
        self._get_api_list = client.get_api_list
