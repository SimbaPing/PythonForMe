# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 19:53:01
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 20:01:39

# 求1!+2!+3!+...+20!的和
s = 0  # 总和
n = 0  # 一共要遍历多少次
t = 1  # 第一个数字是多少
for n in range(1, 21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = %d' % s
