# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 21:07:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 22:14:11

# 还是不太懂
Tn = 0
Sn = []
n = int(raw_input('n =:\n'))
a = int(raw_input('a =:\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x, y: x + y, Sn)
print Sn
