# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: factorial.py
@time: 2017/11/28 23:00
"""

num = int(input("请输入一个数字，来计算阶乘："))
factorial = 1

# 查看数字是负数，0或正数
if num < 0:
    print("抱歉，负数没法阶乘")
elif num == 0:
    print("0的阶乘为1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("%d的阶乘为%d" %(num, factorial))
