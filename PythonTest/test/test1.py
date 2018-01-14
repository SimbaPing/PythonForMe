#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: test1.py
@time: 2018/1/14 23:31
"""

# 输入字符，并以相反的顺序打印出来


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string: ')
l = len(s)
output(s, l)
