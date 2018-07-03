#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: th1.py
@Time: 2018/5/23 14:07
"""

# 从一个区间随意取5个值，比较大小，最大值减去最小值

# 已经完成客厅部分

import random
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 编码格式
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  # 表格名称

kth = 2700  # 客厅高度
ktk = 3590  # 客厅开间
qth = 2720  # 卧室高度
wsaj = 4200  # 卧室1，进深
wsak = 3200  # 卧室1，开间
wsbj = 3790  # 卧室2，进深
wsbk = 3200  # 卧室2，开间
wsck = 2590  # 卧室3，开间

ktha = list(range(kth - 10, kth + 10))
ktka = list(range(ktk - 5, ktk + 5))
m = mm = 2  # 指定行数
ii = 0

for i in range(0, 20):
    booksheet.write(0, i, i)
# 将五个随机数填入指定地点
for i in range(0, 68):
    h15 = random.sample(ktha, 5)
    booksheet.write(m, 0, "客厅")
    booksheet.write(m, 1, kth)
    for hh in range(len(h15)):
        booksheet.write(m, hh + 2, h15[hh])
    h15.sort()
    booksheet.write(m, 11, kth - h15[0])
    booksheet.write(m, 12, h15[4] - h15[0])
    m += 5

# 进深
for i in range(0, 68):
    h34 = random.sample(ktka, 2)
    for hh in range(len(h34)):
        booksheet.write(mm, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mm, 14, h34[1] - h34[0])
    mm += 5

workbook.save('thtest13.xls')

