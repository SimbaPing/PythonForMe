# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-23 12:47:10
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-23 12:55:44

# 一个5位数，判断它是不是回文数。
# 即12321是回文数，个位与万位相同，十位与千位相同。
a = int(raw_input('qingshuru:\n'))  # a是一个整数
x = str(a)  # 将a变成一个字符串
flag = True

for i in range(len(x) / 2):  # 整个长度除以2，留下的是整数部分
    if x[i] != x[- i - 1]:  # 字符串正着排跟倒着排不一样
        flag = False  #返回一个错误的
        break　　# 然后立即中断
if flag:  # 如果是正确的就 该咋咋地
    print 'hui', a
else:
    print 'bushi', a
