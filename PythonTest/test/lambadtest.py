#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: lambadtest.py
@Time: 2018/3/9 3:28
"""


g = lambda x: x + 1

print(g(1))
print(g(2))

# 也可以 lambda x: x + 1(1)


def g(x):
    return x + 1


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x % 3 == 0, foo))
print(map(lambda x: x * 2 + 10, foo))