# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 20:08:13
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 20:24:51

x = int(raw_input('x='))
y = int(raw_input('y='))
z = int(raw_input('z='))
l = [x, y, z]
l.sort()
print l

# 官方解法，有些不懂
list = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    list.append(x)
list.sort()  # 自动排列函数方法
print list
