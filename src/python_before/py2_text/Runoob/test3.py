# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 19:32:38
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 19:47:01
import math

for i in range(100000):
    x = int(math.sqrt(i + 100))  # i +　100的平方根时x
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) & (y * y == i + 268):
        print i
