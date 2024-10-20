#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import subprocess
from typing import Optional


PIP_CONF_CMD_PREFIXS = ['python', '-m', 'pip', 'config']
GLOBAL_TRUSTED_HOST = 'global.trusted-host'
GLOBAL_INDEX_URL = 'global.index-url'


class SubConfig():
    index_url: Optional[str]
    trusted_host: Optional[str]


class PipConfig():
    global_: Optional[SubConfig]


class ConfigPath():
    path: Optional[str]
    exists: bool


class PipPath():
    global_: Optional[ConfigPath]
    site: Optional[ConfigPath]
    user: Optional[ConfigPath]


def cmd_output(cmds: list) -> str:
    return subprocess.check_output(cmds).decode().strip('\n')


def pip_config_set(name: str, value: str) -> bool:
    cmds = [
        'pip',
        'config',
        'set',
        name,
        value
    ]
    res = cmd_output(cmds)
    if 'Writing to' in res:
        return True
    return False


def pip_config_get(name: str):
    cmds = list(PIP_CONF_CMD_PREFIXS)
    cmds.extend([
        'get',
        name
    ])
    return cmd_output(cmds)


def pip_config_list():
    out_byte = subprocess.check_output(['pip', 'config', 'list'])
    out_text = out_byte.decode()
    print(f"-{out_text}-", type(out_text))


def pip_config_debug():
    cmds = list(PIP_CONF_CMD_PREFIXS)
    cmds.extend([
        'debug'
    ])
    return cmd_output(cmds)


def line_to_path(line: str) -> ConfigPath:
    path, exists = line.split(",")
    cp = ConfigPath()
    cp.path = path.strip()
    cp.exists = True if 'True' in exists else False
    return cp


def get_pip_config_path(debug_text: Optional[str] = None) -> PipPath:
    '''获取 pip config 地址'''
    if not debug_text:
        debug_text = pip_config_debug()
    lines = debug_text.split("\n")
    p = PipPath()
    for i, line in enumerate(lines):
        if line == 'global:':
            p.global_ = line_to_path(lines[i+1])
        if line == 'site:':
            p.site = line_to_path(lines[i+1])
        if line == 'user:':
            p.user = line_to_path(lines[i+1])
            if not p.user.exists:
                p.user = line_to_path(lines[i+2])
    return p


def get_user_config() -> Optional[PipConfig]:
    g_conf = SubConfig()

    g_conf.trusted_host = pip_config_get(GLOBAL_TRUSTED_HOST)
    g_conf.index_url = pip_config_get(GLOBAL_INDEX_URL)
    item = PipConfig()
    item.global_ = g_conf
    return item


def pip_config_set_registry(
    index_url: str,
    trusted_host: str,
):
    return (
        pip_config_set(GLOBAL_INDEX_URL, index_url) and
        pip_config_set(GLOBAL_TRUSTED_HOST, trusted_host)
    )
