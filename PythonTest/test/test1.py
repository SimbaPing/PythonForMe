#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: test1.py
@time: 2018/1/14 23:31
"""

# # 输入字符，并以相反的顺序打印出来

def output(one, two):
    if two == 0:
        return
    print(one[two - 1])
    output(one, two - 1)


one = input('Input a string: ')
two = len(one)
output(one, two)

print("hello world!")

print('good')

# 两个列表合为字典
