#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: fibonacci.py
@time: 2017/11/23 1:50
"""

# 传说中的斐波那契数列
# 0,1,1,2,3,5,8……

nf = int(input("想要获得多少个："))

n1 = 0
n2 = 1
count = 2

if nf <= 0:
    print("请输入一个正整数")
elif nf == 1:
    print("斐波那契数列为", n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=",")
    while count < nf:
        nth = n1 + n2
        print(nth, end=",")

        n1 = n2
        n2 = nth
        count += 1
