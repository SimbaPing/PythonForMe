# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-05 21:05:49
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-06 00:56:04


def convert(ok, go):
    'conv. sequence of numbers to same type'
    return [ok(eachNum) for eachNum in go]

mygo = (123, 45.67, -6.2e8, 999999999L)
print convert(int, mygo)
print convert(long, mygo)
print convert(float, mygo)
