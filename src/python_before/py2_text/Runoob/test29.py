# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 23:36:30
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-23 12:46:54

# 给一个不多于5位的正整数，
# 要求：一、求它是几位数，二、逆序打印出各位数字。
x = int(raw_input("请输入一个数:\n"))
a = x / 10000  # 定义五位数的万位
b = x % 10000 / 1000  #　定义五位数的千位
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print "5位数：", e, d, c, b, a
elif b != 0:
    print "four", e, d, c, b
elif c != 0:
    print "three", e, d, c
elif d != 0:
    print "two", e, d
else:
    print "one", e

