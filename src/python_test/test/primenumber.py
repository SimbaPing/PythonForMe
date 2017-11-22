#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: primenumber.py
@time: 2017/11/23 0:29
"""

# 一个大于1的自然数，只能被1和他自己整除
# 关于迭代，条件判断，跳出循环
num = int(input("检查是否为质数："))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "不是质数")
            break
    else:
        print(num, "是质数")
