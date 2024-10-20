#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com

from .registry import (
    get_registry,
    get_registrys,
)
from .http_tools import (
    test_latency
)
from .manager import (
    get_manager,
)


__all__ = [
    'get_registry',
    'get_registrys',
    'test_latency',
    'get_manager',
]
