#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import List, Optional
from urllib.parse import urlparse


class Registry:
    name: str
    index_url: str
    host: str

    def __init__(self, name: str, index_url: str):
        self.name = name
        self.index_url = index_url
        self.host = urlparse(self.index_url).netloc


REGISTRYS = [
    Registry('tencent', 'http://mirrors.cloud.tencent.com/pypi/simple'),
    Registry('tsinghua', 'https://pypi.tuna.tsinghua.edu.cn/simple'),
    Registry('aliyun', 'https://mirrors.aliyun.com/pypi/simple'),
    Registry('edu', 'https://mirrors.ustc.edu.cn/pypi/simple'),
]

REGISTRY_MAP = {o.name: o for o in REGISTRYS}
REGISTRY_URL_MAP = {o.index_url: o for o in REGISTRYS}


def get_registrys() -> List[Registry]:
    REGISTRYS.sort(key=lambda o: o.name)
    return REGISTRYS


def get_registry(name: str) -> Optional[Registry]:
    return REGISTRY_MAP.get(name)


def get_registry_by_url(url: str) -> Optional[Registry]:
    return REGISTRY_URL_MAP.get(url)
