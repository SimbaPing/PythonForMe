# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 14:05:39
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 14:14:12
# 有 1、2、3、4，
# 能够组成多少个互不相同且无重复数字的三位数
# 都是多少

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) & (j != k) & (k != i):
                print i, j, k
# 思路：确定范围用for in range():
#       确定条件 if () and ():
