#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: leapyear.py
@time: 2017/11/22 23:44
"""

# 让判断一个闰年，如果一个数能被 4 和 400 整除，那么这就是闰年
# 有点简陋，但起码是自己编的

isyear = int(input('year: '))

if isyear % 4 == 0 & isyear % 400 == 0:
    print("闰年")
else:
    print("不是闰年")
