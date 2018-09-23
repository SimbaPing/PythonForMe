#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/23 22:22
Filename: roman-to-integer.py
Contact: uppjs@qq.com
Description: 
"""


def romanToInt(s):
    suma = 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s) - 1):
        if convert[s[i]] < convert[s[i + 1]]:
            suma = suma - convert[s[i]]
        else:
            suma = suma + convert[s[i]]
    print(suma + convert[s[-1]])


romanToInt('MDCLXVI')
romanToInt('IVXL')
romanToInt('IVI')