#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
import os
import pathlib
from xmlrpc.client import ServerProxy

from pylinuxauto.config import config
from pylinuxauto.remote.guard import guard_rpc


@guard_rpc
def client(
        user: str,
        ip: str,
        password: str,
        auto_restart: bool = False,
):
    return ServerProxy(f"http://{ip}:{config.RPC_PORT}", allow_none=True)
