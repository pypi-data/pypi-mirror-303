#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typing import Optional
from piprm.registry import (
    Registry,
)
from .factory import register_manager, BaseManager

PIP_CONF_CMD_PREFIXS = ['python', '-m', 'pip', 'config']
GLOBAL_TRUSTED_HOST = 'global.trusted-host'


@register_manager
class PipManager(BaseManager):
    class Meta():
        # 管理器名称
        name: str = 'pip'
        key_index_url: str = 'global.index-url'

    def set_registry(self, name: str) -> bool:
        r = self.get_registry(name)
        return (
            self.set_config(self.Meta.key_index_url, r.index_url) and
            self.set_config(GLOBAL_TRUSTED_HOST, r.host)
        )

    def set_config(self, name: str, value: str):
        cmds = list(PIP_CONF_CMD_PREFIXS)
        cmds.extend([
            'set',
            name,
            value
        ])
        res = self.cmd_output(cmds)
        if 'Writing to' in res:
            return True
        return False

    def get_config(self, name: str) -> str:
        cmds = list(PIP_CONF_CMD_PREFIXS)
        cmds.extend([
            'get',
            name
        ])
        return self.cmd_output(cmds)
