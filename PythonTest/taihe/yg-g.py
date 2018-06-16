#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: yg-g.py
@Time: 2018/6/16 21:46
"""

import random
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 编码格式
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  # 表格名称
kth = 2680  # 客厅高度
ktj = 3610  # 客厅进深
qath = 2720  # 卧12书房高度
qbth = 2720  # 卧3高度
wsak = 3350  # 卧室1，开间
wsaj = 3640  # 卧室1，进深
wsbj = 2790  # 卧室2，进深
wsbk = 2050  # 卧室2，开间
wsck = 3190  # 卧室3，开间
wscj = 3600  # 卧室3，进深
ktha = list(range(kth - 10, kth + 10))
ktja = list(range(ktj - 10, ktj + 10))
qatha = list(range(qath - 10, qath + 10))
qbtha = list(range(qbth - 10, qbth + 10))
wsaka = list(range(wsak - 10, wsak + 10))
wsaja = list(range(wsaj - 10, wsaj + 10))
wsbja = list(range(wsbj - 10, wsbj + 10))
wsbka = list(range(wsbk - 10, wsbk + 10))
wscka = list(range(wsck - 10, wsck + 10))
wscja = list(range(wscj - 10, wscj + 10))

ttt = 23  # 一共生成几组

n = 1
n1 = 1
m = m1 = m0 = 2  # 指定行数
ma = mb = mc = 3
maa = mbb = mcc = 4
md = me = mf = 5
m00 = m11 = m22 = 6

# 序号栏
for i in range(0, ttt):
    print(i)
    for nn in range(0, 10):
        booksheet.write(n, nn, i + 1)
    print(n)
    n += 6

# 客厅高度
for i in range(0, ttt):  # 一共生成6组
    h15 = random.sample(ktha, 5)  # 在这个列表里随机选5个数
    booksheet.write(m, 0, "客厅")  # 这里填入“客厅”
    booksheet.write(m, 1, kth)  # 这里填入 kth
    for hh in range(len(h15)):  # 将这5个随机数填进相应的位置
        booksheet.write(m, hh + 2, h15[hh])
    h15.sort()  # 为了好排列，将五个数从小到大排列
    booksheet.write(m, 11, abs(kth - h15[0]))  # 标准值与最小值的差
    booksheet.write(m, 12, h15[4] - h15[0])  # 最大值减去最小值
    m += 6  # 每隔六行生成一组

# 客厅开间

# 客厅 进深
for i in range(0, ttt):
    h34 = random.sample(ktja, 2)
    for hh in range(len(h34)):
        booksheet.write(m1, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(m1, 13, h34[1] - h34[0])
    m1 += 6

# 卧室1 高度
for i in range(0, ttt):
    h15 = random.sample(qatha, 5)
    booksheet.write(ma, 0, "卧1")
    booksheet.write(ma, 1, qath)
    for hh in range(len(h15)):
        booksheet.write(ma, hh + 2, h15[hh])
    h15.sort()
    booksheet.write(ma, 11, abs(kth - h15[0]))
    booksheet.write(ma, 12, h15[4] - h15[0])
    ma += 6

# 卧室1 开间
for i in range(0, ttt):
    h34 = random.sample(wsaka, 2)
    for hh in range(len(h34)):
        booksheet.write(mc, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mc, 14, h34[1] - h34[0])
    mc += 6

# 卧室1 进深 111111111111111111111111111111
for i in range(0, ttt):
    h34 = random.sample(wsaja, 2)
    for hh in range(len(h34)):
        booksheet.write(mb, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mb, 13, h34[1] - h34[0])
    mb += 6

# 卧室2 高度
for i in range(0, ttt):
    h15 = random.sample(qbtha, 5)
    booksheet.write(maa, 0, "卧2")
    booksheet.write(maa, 1, qbth)
    for hh in range(len(h15)):
        booksheet.write(maa, hh + 2, h15[hh])
    h15.sort()
    booksheet.write(maa, 11, abs(kth - h15[0]))
    booksheet.write(maa, 12, h15[4] - h15[0])
    maa += 6

# 卧室2 开间
for i in range(0, ttt):
    h34 = random.sample(wsbka, 2)
    for hh in range(len(h34)):
        booksheet.write(mcc, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mcc, 14, h34[1] - h34[0])
    mcc += 6

# 卧室2 进深
for i in range(0, ttt):
    h34 = random.sample(wsbja, 2)
    for hh in range(len(h34)):
        booksheet.write(mbb, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mbb, 13, h34[1] - h34[0])
    mbb += 6

# 卧室3 高度
for i in range(0, ttt):
    h15 = random.sample(qbtha, 5)
    booksheet.write(md, 0, "卧3")
    booksheet.write(md, 1, qbth)
    for hh in range(len(h15)):
        booksheet.write(md, hh + 2, h15[hh])
    h15.sort()
    booksheet.write(md, 11, abs(kth - h15[0]))
    booksheet.write(md, 12, h15[4] - h15[0])
    md += 6

# 卧室3 进深
for i in range(0, ttt):
    h34 = random.sample(wscja, 2)
    for hh in range(len(h34)):
        booksheet.write(mf, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(mf, 13, h34[1] - h34[0])
    mf += 6

# 卧室3 开间
for i in range(0, ttt):
    h34 = random.sample(wscka, 2)
    for hh in range(len(h34)):
        booksheet.write(me, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(me, 14, h34[1] - h34[0])
    me += 6


workbook.save('7#东单元东2-7共6.xls')
