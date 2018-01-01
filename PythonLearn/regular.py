#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: regular.py
@time: 2017/12/30 20:48
"""
import re

"""
1.基础
1.1 原始字符串 r'expressin'
1.2 匹配单个字符的基本模式，好多...
1.3 编译标志，可以修改正则表达式的某些方面。IGNORECASE 或 I
2. match 和 search
2.1 re.match(pattern, string, flags=0) 与 re.search(pattern, string, flags=0)
    pattern - 这是要匹配的正则表达式。
    string - 这是字符串，它将被搜索用于匹配字符串开头的模式。 |
    flags - 可以使用按位OR(|)指定不同的标志。 这些是修饰符，如下表所列
"""
# 2.2 match 将 re 模式和可选标志的字符串进行匹配，成功时候返回匹配对象，失败是返回 none
# 2.3 group(num = 0)	此方法返回整个匹配(或特定子组num)
#     groups()	此方法返回一个元组中的所有匹配子组(如果没有，则返回为None)
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # 每一个小括号都是一个 group()

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.groups():", matchObj.groups())  # 只返回元组中的值，形式：元组中的字符串
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!!")
