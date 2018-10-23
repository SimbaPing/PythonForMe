#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/12 10:17
Filename: t-count-primes.py
Contact: uppjs@qq.com
Description: 
"""


def countPrimes(num):
    if num == 0 or num == 1:
        print(0)
    for i in range(1, num):
        print(i)


countPrimes(2)
