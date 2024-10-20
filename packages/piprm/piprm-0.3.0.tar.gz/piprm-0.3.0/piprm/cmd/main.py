#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import typer
from typer import Option, Argument
from typing import Optional
from piprm import (
    get_registry,
    get_registrys,
    test_latency,
    get_manager,
)


app = typer.Typer()

OPTION_MANAGER = Option('pip', '-m', '--manager', help='管理器')


@app.command()
def ls(
    manager_name: str = OPTION_MANAGER,
):
    registrys = get_registrys()
    m = get_manager(manager_name)
    use_registry = m.get_use_registry()
    is_use = False
    for r in registrys:
        name = f"{r.name} "
        if use_registry and use_registry.name == r.name:
            is_use = True
        use = '*' if is_use else ' '
        print(f"{use} {name:-<20} {r.index_url}")
        is_use = False


@app.command()
def use(
    name: str = Argument(help='registry name'),
    manager_name: str = OPTION_MANAGER,
):
    m = get_manager(manager_name)
    m.set_registry(name)
    msg = f"The registry has been changed to '{name}'."
    print(msg)


@app.command()
def test(
    name: Optional[str] = Option(None, help='Registry name')
):
    if name:
        r = get_registry(name)
        t = test_latency(r.index_url)
        print(f"{name} ------ {t} ms")
    else:
        registrys = get_registrys()
        for r in registrys:
            t = test_latency(r.index_url)
            print(f"{r.name} ------ {t} ms")


@app.command()
def version():
    print('prm 0.3.0')


if __name__ == "__main__":
    app()
