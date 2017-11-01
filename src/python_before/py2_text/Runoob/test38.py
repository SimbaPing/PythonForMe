# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 18:07:41
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 18:14:49

# 求一个3*3矩阵对角线元素之和
# 什么鬼，看不懂会不会很丢人
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input('input num:\n')))

    for i in range(3):
        sum += a[i][i]
    print sum
