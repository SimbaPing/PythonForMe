#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/7 5:35
Filename: t-reverse-words-in-a-string.py
Contact: uppjs@qq.com
Description: 
"""

s1 = "Let's take LeetCode contest"
s3 = []
s2 = s1.split(" ")  # 将字符串以空格为间隔转换为列表
print(s2)
for i in s2:
    s3.append(i[::-1])  # 每个字符串转换并放入列表

s4 = " ".join(s3)  # 列表转字符串
print(s4)
