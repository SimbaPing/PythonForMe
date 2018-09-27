#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/27 22:06
Filename: t-valid-parentheses.py
Contact: uppjs@qq.com
Description: 
"""

"""
1. 如果是奇数，false
2. 如果是空， false
3. 如果开始是右括号，false
"""

ls = '}{'


def isValid(s):
    f1 = ['(', ')']
    f2 = ['[', ']']
    f3 = ['{', '}']
    if s is None or len(s) % 2 != 0 or s[0] == f1[1] or s[0] == f2[1] or s[0] == f3[1]:
        return False
    else:
        for i in range(len(ls)):
            return



print(isValid(ls))
