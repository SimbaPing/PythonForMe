#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: re_1.py
@time: 2018/1/11 10:28
"""

import re

# 将正则表达式编译成 pattern 对象
pattern = re.compile(r'hello')

# 使用 pattern 匹配文本，获得匹配结果，无法匹配时返回 none
match = pattern.match('hello world!')

if match:
    # 使用 match 获得分组信息
    print(match.group())

p1 = 'hello world!'
p2 = 'one1two2three3four4'
s = 'i say, hello world!'

pattern1 = re.compile(r'world')
match1 = pattern1.search(p1)
print(match1.group())

pattern2 = re.compile(r'\d+')
print(pattern2.split(p2))
print(pattern2.findall(p2))
for m in pattern2.finditer(p2):
    print(m.group())

pattern3 = re.compile(r'(\w) (\w)')
print(pattern3.sub(r'\2 \1', s))
