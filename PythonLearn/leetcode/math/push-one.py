#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/7 5:56
Filename: push-one.py
Contact: uppjs@qq.com
Description: 
"""

s = [4, 3, 2, 1]

s1 = s[len(s) - 1] + 1
del(s[len(s) - 1])
print(s)
print(s1)
s.append(s1)
print(s)

a = '1234'
print(list(a))
number_a = list(map(int, a))  # 数字字符串转数字列表
# 数字列表转数字
print(number_a)

b2 = []
b = [1, 2, 3, 4]
for i in b:
    b2.append(str[i])
    print(b2)

print(b1)


'''
1. 字符串转列表
2. 列表最后一项 +1
'''
