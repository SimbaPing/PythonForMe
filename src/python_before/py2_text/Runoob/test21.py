# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 09:49:11
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 10:00:03

x2 = 1
for day in range(9, 0, -1):  # 倒着循环
    x1 = (x2 + 1) * 2
    x2 = x1
print x1
