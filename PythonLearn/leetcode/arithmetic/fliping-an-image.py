#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/23 0:25
Filename: fliping-an-image.py
Contact: uppjs@qq.com
Description: 
"""

A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

for i in range(len(A)):  # 整个列表的长度
    for j in range(len(A[0])):  # 嵌套列表的长度
        A[i][j] = 1 - int(A[i][j])  # 第 i 个小表中第 j 个数，列表等于1减去它本身（也就是所谓的01替换）
    A[i] = A[i][::-1]  # 替换完成后完成逆序操作

print(A)
