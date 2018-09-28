#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/29 0:06
Filename: learn-dict.py
Contact: uppjs@qq.com
Description: 字典的学习
"""
from operator import *

dict1 = {"abc": 456}
dict2 = {"abc": 123, 98.6: 37}

dict0 = {"Name": "Zara", "Age": 7, "Class": "First"}
dict00 = {"Name": "Zara", "Age": 10, "Class": "First"}
print(dict0)
print(dict0["Name"])
print(is_(dict0, dict00))

ls = []
dicta = {'(': ')', '[': ']', '{': '}'}
for d in '({})':
    if d in dicta:
        ls.append(d)
        print(ls)
