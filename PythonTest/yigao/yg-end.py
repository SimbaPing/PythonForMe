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
yg = [2700, 0, 3990, 2720, 0, 0, 0, 0, 0, 0, 0, 2720, 3010, 2190]
"""
7东东2-7：[2680, 3610, 0, 2720, 3640, 3350, 2720, 2790, 2050, 2720, 3600,
 3190, 0, 0, 0]
7东西2-7：[2700, 0, 3490, 2720, 0, 3200, 2720, 2890, 2750, 2720, 2550,
 2070, 0, 0, 0]
7中东2-18：[2700, 0, 3590, 2720, 4700, 3200, 2720, 3290, 3200, 2720, 0,
 2590, 0, 0, 0]
9西西1-18：[2700, 0, 3890, 2710, 0, 3350, 2720, 3510, 2890, 2720, 2590,
 2090, 0, 0, 0]
9西东-中西-1-18： [2690, 0, 3910, 2710, 0, 3380, 2710, 4110, 3380, 2720,
 0, 2780, 0, 0, 0]
8西西1-18: [2700, 0, 3880, 2720, 0, 3400, 2680, 4100, 2590, 2720, 0,
 3200, 0, 0, 0]
8西东-东西-1-18：[2700, 0, 3880, 2720, 0, 3390, 2680, 4100, 2580, 2720,
 0, 3200, 0, 0, 0]
9东西-中东-1-18：[2690, 0, 3910, 2700, 0, 3390, 2710, 4090, 3390, 2720,
 0, 2780, 0, 0, 0]
4东1-23：[2770, 0, 3750, 2780, 0, 3380, 2790, 0, 2580, 2790, 0, 3090, 0, 0, 0]
7中西-西东-2-18：[2700, 0, 3590, 2720, 4200, 3190, 2720, 3690, 2550, 2720,
 0, 2590, 0, 0, 0]
7西西2-18：[2700, 0, 3590, 2720, 4200, 3200, 2720, 3790, 3200, 2720, 0,
 2590, 0, 0, 0]
8东东1-18：[2700, 0, 3990, 2720, 0, 3400, 2720, 3290, 3410, 2720, 0, 2990,
 2720, 3010, 2190]
9东东1-18：[2690, 0, 3970, 2700, 0, 3410, 2710, 3390, 3410, 2710, 0, 3350,
 2720, 3110, 3290]
"""
kth = yg[0]  # 客厅高度
ktj = yg[1]  # 客厅进深
ktk = yg[2]  # 客厅开间
wsah = yg[3]  # 卧室高度
wsaj = yg[4]  # 卧室1，进深
wsak = yg[5]  # 卧室1，开间
wsbh = yg[6]  # 我是1，高度
wsbj = yg[7]  # 卧室2，进深
wsbk = yg[8]  # 卧室2，开间
wsch = yg[9]  # 卧室3，高度
wscj = yg[10]  # 卧室3，进深
wsck = yg[11]  # 卧室3，开间
wsdh = yg[12]
wsdj = yg[13]
wsdk = yg[14]

ktha = list(range(kth - 9, kth + 9))
ktja = list(range(ktj - 9, ktj + 9))
ktka = list(range(ktk - 9, ktk + 9))
wsaha = list(range(wsah - 9, wsah + 9))
wsaja = list(range(wsaj - 9, wsaj + 9))
wsaka = list(range(wsak - 9, wsak + 9))
wsbha = list(range(wsbh - 9, wsbh + 9))
wsbja = list(range(wsbj - 9, wsbj + 9))
wsbka = list(range(wsbk - 9, wsbk + 9))
wscha = list(range(wsch - 9, wsch + 9))
wscja = list(range(wscj - 9, wscj + 9))
wscka = list(range(wsck - 9, wsck + 9))
wsdha = list(range(wsdh - 9, wsdh + 9))
wsdja = list(range(wsdj - 9, wsdj + 9))
wsdka = list(range(wsdk - 9, wsdk + 9))

ttt = 50  # 一共生成几组

n = 1
n1 = 1
m = m1 = m0 = 2  # 指定行数
ma = mb = mc = 3
maa = mbb = mcc = 4
md = me = mf = 5
maaa = mbbb = mccc = 6

# 序号栏
for i in range(0, ttt):
    for nn in range(0, 10):
        booksheet.write(n, nn, i + 1)
    n += 6

# 客厅高度
for i in range(0, ttt):  # 一共生成6组
    h15 = random.sample(ktha, 5)  # 在这个列表里随机选5个数
    booksheet.write(m, 0, "客厅")  # 这里填入“客厅”
    booksheet.write(m, 1, kth)  # 这里填入 kth
    for hh in range(len(h15)):  # 将这5个随机数填进相应的位置
        booksheet.write(m, hh + 2, h15[hh])
    h15.sort()  # 为了好排列，将五个数从小到大排列
    if abs(h15[0] - kth) >= abs(h15[4] - kth):
        booksheet.write(m, 11, h15[0] - kth)
    else:
        booksheet.write(m, 11, h15[4] - kth)
    # booksheet.write(m, 11, abs(kth - h15[0]))  # 标准值与最小值的差
    booksheet.write(m, 12, h15[4] - h15[0])  # 最大值减去最小值
    m += 6  # 每隔六行生成一组

# 客厅开间
if ktk != 0:
    for i in range(0, ttt):
        h34 = random.sample(ktka, 2)
        for hh in range(len(h34)):
            booksheet.write(m0, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(m0, 14, h34[1] - h34[0])
        m0 += 6

# 客厅 进深
if ktj != 0:
    for i in range(0, ttt):
        h34 = random.sample(ktja, 2)
        for hh in range(len(h34)):
            booksheet.write(m1, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(m1, 13, h34[1] - h34[0])
        m1 += 6

# 卧室1 高度
for i in range(0, ttt):
    h15 = random.sample(wsaha, 5)
    booksheet.write(ma, 0, "卧1")
    booksheet.write(ma, 1, wsah)
    for hh in range(len(h15)):
        booksheet.write(ma, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - wsah) >= abs(h15[4] - wsah):
        booksheet.write(ma, 11, h15[0] - wsah)
    else:
        booksheet.write(ma, 11, h15[4] - wsah)
    # booksheet.write(ma, 11, abs(kth - h15[0]))
    booksheet.write(ma, 12, h15[4] - h15[0])
    ma += 6

# 卧室1 开间
if wsak != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsaka, 2)
        for hh in range(len(h34)):
            booksheet.write(mc, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mc, 14, h34[1] - h34[0])
        mc += 6

# 卧室1 进深 111111111111111111111111111111
if wsaj != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsaja, 2)
        for hh in range(len(h34)):
            booksheet.write(mb, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mb, 13, h34[1] - h34[0])
        mb += 6

# 卧室2 高度
for i in range(0, ttt):
    h15 = random.sample(wsbha, 5)
    booksheet.write(maa, 0, "卧2")
    booksheet.write(maa, 1, wsbh)
    for hh in range(len(h15)):
        booksheet.write(maa, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - wsbh) >= abs(h15[4] - wsbh):
        booksheet.write(maa, 11, h15[0] - wsbh)
    else:
        booksheet.write(maa, 11, h15[4] - wsbh)
    # booksheet.write(maa, 11, abs(kth - h15[0]))
    booksheet.write(maa, 12, h15[4] - h15[0])
    maa += 6

# 卧室2 开间
if wsbk != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsbka, 2)
        for hh in range(len(h34)):
            booksheet.write(mcc, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mcc, 14, h34[1] - h34[0])
        mcc += 6

# 卧室2 进深
if wsbj != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsbja, 2)
        for hh in range(len(h34)):
            booksheet.write(mbb, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mbb, 13, h34[1] - h34[0])
        mbb += 6

# 卧室3 高度
for i in range(0, ttt):
    h15 = random.sample(wscha, 5)
    booksheet.write(md, 0, "卧3")
    booksheet.write(md, 1, wsch)
    for hh in range(len(h15)):
        booksheet.write(md, hh + 2, h15[hh])
    h15.sort()
    if abs(h15[0] - wsch) >= abs(h15[4] - wsch):
        booksheet.write(md, 11, h15[0] - wsch)
    else:
        booksheet.write(md, 11, h15[4] - wsch)
    # booksheet.write(md, 11, abs(kth - h15[0]))
    booksheet.write(md, 12, h15[4] - h15[0])
    md += 6

# 卧室3 进深
if wscj != 0:
    for i in range(0, ttt):
        h34 = random.sample(wscja, 2)
        for hh in range(len(h34)):
            booksheet.write(mf, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mf, 13, h34[1] - h34[0])
        mf += 6

# 卧室3 开间
if wsck != 0:
    for i in range(0, ttt):
        h34 = random.sample(wscka, 2)
        for hh in range(len(h34)):
            booksheet.write(me, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(me, 14, h34[1] - h34[0])
        me += 6

# 书房 高度
if wsdh != 0:
    for i in range(0, ttt):
        h15 = random.sample(wsdha, 5)
        booksheet.write(maaa, 0, "书房")
        booksheet.write(maaa, 1, wsdh)
        for hh in range(len(h15)):
            booksheet.write(maaa, hh + 2, h15[hh])
        h15.sort()
        if abs(h15[0] - wsdh) >= abs(h15[4] - wsdh):
            booksheet.write(maaa, 11, h15[0] - wsdh)
        else:
            booksheet.write(maaa, 11, h15[4] - wsdh)
        # booksheet.write(maaa, 11, abs(kth - h15[0]))
        booksheet.write(maaa, 12, h15[4] - h15[0])
        maaa += 6

# 书房 进深
if wsdj != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsdja, 2)
        for hh in range(len(h34)):
            booksheet.write(mbbb, hh + 7, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mbbb, 13, h34[1] - h34[0])
        mbbb += 6

# 书房 开间
if wsdk != 0:
    for i in range(0, ttt):
        h34 = random.sample(wsdka, 2)
        for hh in range(len(h34)):
            booksheet.write(mccc, hh + 9, h34[hh])  # 第 m 行，第 hh-1 格，填入 h34[hh]
        h34.sort()
        booksheet.write(mccc, 14, h34[1] - h34[0])
        mccc += 6

workbook.save('8东东1-18.xls')
