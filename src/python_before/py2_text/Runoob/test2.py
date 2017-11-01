# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 14:14:20
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 19:32:28
i = int(raw_input('净利润：'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print (i - arr[idx]) * rat[idx]
        i = arr[idx]
print r
# 这个数学公式有点复杂，好难懂
