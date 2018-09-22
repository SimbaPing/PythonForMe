#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/22 23:10
Filename: t-flipping-an-image.py
Contact: uppjs@qq.com
Description: 
"""

list_start = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
list_a = []
list_b = []

length = len(list_start)
for i in range(length):
    for j in range(i + 1, length):
        temp = list_start[i][j]
        print(temp)
        list_start[i][j] = list_start[j][i]
        list_start[j][i] = temp
        print(list_start[j][i])
for i in range(len(list_start)):
    list_start[i] = list_start[i][::-1]

print(list_start[i])
