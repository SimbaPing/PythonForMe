#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 9/21/2018 06:25
Filename: pa-number-t.py
Contact: uppjs@qq.com
Description: 
"""

x = "abccba"
y = []
# 将字符串转换为列表
list_x = list(x)
for i in range(len(list_x)):
    y.append(list_x[len(list_x) - 1 - i])

y = "".join(y)
print(str(y))
print(x == y)

x_input = input("look: ")
print(type(x_input))
y_input = x_input[::-1]
if y_input == x_input:
    print("Fuck!")
