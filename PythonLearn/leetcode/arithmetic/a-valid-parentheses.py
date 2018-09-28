#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/28 23:54
Filename: a-valid-parentheses.py
Contact: uppjs@qq.com
Description: 有效的括号
"""


def isValid(s):
    stack = []
    lookup = {'(': ')', '[': ']', '{': '}'}
    for parenthese in s:
        if parenthese in lookup:
            stack.append(parenthese)
        elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
            return False
    return len(stack) == 0


s1 = '()(('
s2 = '({})'
print(isValid(s1))
print(isValid(s2))
