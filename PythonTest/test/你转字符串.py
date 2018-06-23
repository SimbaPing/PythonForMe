# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.....author: Ping
....contact: uppjs@qq.com
.......file: 你转字符串.py
.......time: 2018/06/23 22:01:02
Created with Visual Studio Code.
description:
"""


def rev(s):
    a = list(s)
    a.reverse()
    return (''.join(a))


a = rev(input("输入一些东西"))
print(a)
