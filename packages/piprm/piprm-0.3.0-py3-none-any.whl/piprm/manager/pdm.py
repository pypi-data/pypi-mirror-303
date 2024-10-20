#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typing import Optional
from piprm.registry import (
    Registry,
    get_registrys,
    get_registry,
    get_registry_by_url,
)
from .factory import register_manager, BaseManager

GLOBAL_TRUSTED_HOST = 'global.trusted-host'
GLOBAL_INDEX_URL = 'global.index-url'


@register_manager
class PdmManager(BaseManager):
    class Meta():
        # 管理器名称
        name: str = 'pdm'
        key_index_url: str = 'pypi.url'

    def set_registry(self, name: str) -> bool:
        r = self.get_registry(name)
        return (
            self.set_config(self.Meta.key_index_url, r.index_url)
        )

    def set_config(self, name: str, value: str):
        cmds = [
            'pdm',
            'config',
            name,
            value
        ]
        self.cmd_output(cmds)
        return True

    def get_config(self, name: str) -> str:
        cmds = [
            'pdm',
            'config',
            name,
        ]
        return self.cmd_output(cmds)
