#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/6 4:40
Filename: single-number.py
Contact: uppjs@qq.com
Description: 只出现一次的数字
"""


def singleNumber(nums):
    result = 0
    for j in nums:
        result ^= j
    return print(result)


def singleNumber1(nums):
    s = []
    for i in nums:
        if i not in s:
            s.append(i)
        elif i in s:
            s.remove(i)

    return print(s[0])


singleNumber([4, 1, 2, 1, 2])
