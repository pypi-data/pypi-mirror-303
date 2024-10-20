#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import subprocess
from abc import ABCMeta, abstractmethod
from typing import Dict, Type, Optional, Tuple, Union
from piprm.registry import (
    Registry,
    get_registry,
    get_registry_by_url,
)
from piprm.exceptions import RegistryException


class BaseManager(metaclass=ABCMeta):
    class Meta():
        # 管理器名称
        name: str
        key_index_url: str

    @abstractmethod
    def set_registry(self, name: str) -> bool:
        ...

    def get_use_registry(self) -> Optional[Registry]:
        index_url = self.get_config(self.Meta.key_index_url)
        return get_registry_by_url(index_url)

    @abstractmethod
    def set_config(self, name: str, value: str) -> bool:
        ...

    @abstractmethod
    def get_config(self, name: str) -> str:
        ...

    def cmd_output(self, cmds: list) -> str:
        return subprocess.check_output(cmds).decode().strip('\n')

    def get_registry(self, name: str) -> Optional[Registry]:
        r = get_registry(name)
        if not r:
            raise RegistryException(f"registry {name} not found")
        return r


_manager_map: Dict[str, BaseManager] = {}


def register_manager(cls: Type[BaseManager]):
    '''添加管理器'''
    _manager_map[cls.Meta.name] = cls()
    return cls


def get_manager(name: str) -> Optional[BaseManager]:
    return _manager_map.get(name)
