#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: ninenine.py
@time: 2017/11/21 0:58
other: 这是一个九九乘法表，两层迭代（iterate）
"""

for i in range(1, 10):  # 第一个数字从1至9
    for j in range(1, i + 1):  # 第二个数字的取值
        print('{}x{}={}\t'.format(i, j, i * j,), end='')  # 将两个数字结合起来的算法
    print()  # 打印空行
