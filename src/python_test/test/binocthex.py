# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: binocthex.py
@time: 2017/11/23 22:35
"""
# 将十进制数转换为二进制、八进制、十六进制
a = int(input("输入数字（仅限十进制）："))

print("十进制数为：", a)
print("八进制数为：", oct(a))
print("二进制数为：", bin(a))
print("十六进制数为：", hex(a))
