#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: strnum.py
@time: 2018/1/25 10:01
"""

# 判断一个字符串是否是数字


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


print(is_number('foo'))
print(is_number('1'))
print(is_number(input('测试这个字符串是否为数字：')))
