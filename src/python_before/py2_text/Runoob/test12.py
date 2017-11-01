# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 13:14:38
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 13:25:06

# 判断101-200之间有多少个素数， 并输出所有素数

from math import sqrt
import sys
h = 0
leap = 1
for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '% - 4d' % m
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d' % h

# 有些不懂，数学有点难，公式也有点绕
