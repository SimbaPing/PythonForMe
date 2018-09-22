#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/22 23:10
Filename: t-flipping-an-image.py
Contact: uppjs@qq.com
Description: 
"""

ls = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
list_a = []
list_b = []

length = len(ls)
for i in range(length):
    for j in range(i + 1, length):
        temp = ls[i][j]
        print(temp)
        ls[i][j] = ls[j][i]
        ls[j][i] = temp
        print(ls[j][i])
    for i in range(len(ls)):
        ls[i] = ls[i][::-1]

for i in range(len(ls)):  # 整个列表的长度
    for j in range(len(ls[0])):  # 嵌套列表的长度
        ls[i][j] = 1 - int(ls[i][j])  # 第 i 个小表中第 j 个数，列表等于1减去它本身
    ls[i] = ls[i][::-1]  #

print(ls)
