#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: yg-b.py
@Time: 2018/6/16 17:50
"""

import random
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 编码格式
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  # 表格名称
kth = 2700  # 客厅高度

ktk = 3590  # 客厅开间
qth = 2720  # 卧室高度
wsaj = 4700  # 卧室1，进深
wsak = 3200  # 卧室1，开间
wsbj = 3290  # 卧室2，进深
wsbk = 3200  # 卧室2，开间
wsck = 2590  # 卧室3，开间

ktha = list(range(kth - 9, kth + 9))
ktka = list(range(ktk - 9, ktk + 9))
qtha = list(range(qth - 9, qth + 9))
wsaja = list(range(wsaj - 9, wsaj + 9))
wsaka = list(range(wsak - 9, wsak + 9))
wsbja = list(range(wsbj - 9, wsbj + 9))
wsbka = list(range(wsbk - 9, wsbk + 9))
wscka = list(range(wsck - 9, wsck + 9))

ttt = 17  # 一共生成几组

n = 1
n1 = 1
m = m1 = m0 = 2  # 指定行数
ma = mb = mc = 3
maa = mbb = mcc = 4
md = me = 5

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
    if abs(h15[0] - kth) > abs(h15[4] - kth):
        booksheet.write(m, 11, h15[0] - kth)
    else:
        booksheet.write(m, 11, h15[4] - kth)
    # booksheet.write(m, 11, abs(kth - h15[0]))  # 标准值与最小值的差
    booksheet.write(m, 12, h15[4] - h15[0])  # 最大值减去最小值
    m += 6  # 每隔六行生成一组

# 客厅开间
for i in range(0, ttt):
    h34 = random.sample(ktka, 2)
    for hh in range(len(h34)):
        booksheet.write(m0, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(m0, 14, h34[1] - h34[0])
    m0 += 6

# 客厅 进深


# 卧室1 高度
for i in range(0, ttt):
    h15 = random.sample(qtha, 5)
    booksheet.write(ma, 0, "卧1")
    booksheet.write(ma, 1, qth)
    for hh in range(len(h15)):
        booksheet.write(ma, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - qth) > abs(h15[4] - qth):
        booksheet.write(ma, 11, h15[0] - qth)
    else:
        booksheet.write(ma, 11, h15[4] - qth)
    # booksheet.write(ma, 11, abs(kth - h15[0]))
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
    h15 = random.sample(qtha, 5)
    booksheet.write(maa, 0, "卧2")
    booksheet.write(maa, 1, qth)
    for hh in range(len(h15)):
        booksheet.write(maa, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - qth) > abs(h15[4] - qth):
        booksheet.write(maa, 11, h15[0] - qth)
    else:
        booksheet.write(maa, 11, h15[4] - qth)
    # booksheet.write(maa, 11, abs(kth - h15[0]))
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
    h15 = random.sample(qtha, 5)
    booksheet.write(md, 0, "卧3")
    booksheet.write(md, 1, qth)
    for hh in range(len(h15)):
        booksheet.write(md, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - qth) > abs(h15[4] - qth):
        booksheet.write(md, 11, h15[0] - qth)
    else:
        booksheet.write(md, 11, h15[4] - qth)
    # booksheet.write(md, 11, abs(kth - h15[0]))
    booksheet.write(md, 12, h15[4] - h15[0])
    md += 6

# 卧室3 进深


# 卧室3 开间
for i in range(0, ttt):
    h34 = random.sample(wscka, 2)
    for hh in range(len(h34)):
        booksheet.write(me, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
    h34.sort()
    booksheet.write(me, 14, h34[1] - h34[0])
    me += 6

workbook.save('7#中单元东2-18共17-h.xls')
