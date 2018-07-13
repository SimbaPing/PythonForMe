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
yg = [2700, 3880, 0, 2720, 3400, 0, 2680, 2590, 4100, 2720, 3200, 0, 0, 0, 0]

"""
开间进深的位置填反了，但因为公式一样，所以不做更改。
7东东2-7：[2680,0,3610,2720,3350,3640,2720,2050,2790,2720,3190,3600,0,0,0]
7东西2-7：[2700,3490,0,2720,3200,0,2720,2750,2890,2720,2070,2550,0,0,0]
7中东2-18：[2700,3590,0,2720,3200,4700,2720,3200,3290,2720,2590,0,0,0,0]
9西西1-18：[2700,3890,0,2710,3350,0,2720,2890,3510,2720,2090,2590,0,0,0]
9西东-中西-1-18：
[2690,3910,0,2710,3380,0,2710,3380,0,2710,3380,4110,2720,2780,0,0,0,0]
8西西1-18: [2700，3880，0,2720,3400,0,2680,2590,4100,2720,3200,0,0,0,0]
8西东-东西-1-18：[2700,3880,0,2720,3390,0,2680,2580,4100,2720,3200,0,0,0,0]
9东西-中东-1-18：[2690,3910,0,2700,3390,0,2710,3390,4090,2720,2780,0,0,0,0]
4东1-23：[2770, 0, 3750, 2780, 0, 3380, 2790, 0, 2580, 2790, 0, 3090, 0, 0, 0]
7中西-西东-2-18：[2700,3590,0,2720,3190,4200,2720,2550,3690,2720,2590,0,0,0,0]
7西西2-18：[2700,3590,0,2720,3200,4200,2720,3200,3790,2720,2590,0,0,0,0]
8东东1-18：[2700,3990,0,2720,3400,0,2720,3410,3290,2720,2990,0,2720,2190,3010]
9东东1-18：[2690,3970,0,2700,3410,0,2710,3410,3390,2710,3350,0,2720,3290,3110]
4西西1-23：[2760,7070,3680,2780,3590,0,2780,3530,3900,2790,3220,3280,2780,3400,0]
4西东1-23：[2770,3850,0,2780,3380,0,2790,2680,3980,2790,3190,3280,0,0,0]
8西西1-18：[2700,3880,0,2720,3400,0,2680,2590,4100,2720,3200,0,0,0,0]
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
wsdh = yg[12]  # 卧室4，高度
wsdj = yg[13]  # 卧室4，进深
wsdk = yg[14]  # 卧室4，开间

ktha = list(range(kth - random.randint(3, random.randint(4, 9)),
                  kth + random.randint(3, random.randint(4, 9))))
ktja = list(range(ktj - random.randint(3, random.randint(4, 9)),
                  ktj + random.randint(3, random.randint(4, 9))))
ktka = list(range(ktk - random.randint(3, random.randint(4, 9)),
                  ktk + random.randint(3, random.randint(4, 9))))
wsaha = list(range(wsah - random.randint(3, random.randint(4, 9)),
                   wsah + random.randint(3, random.randint(4, 9))))
wsaja = list(range(wsaj - random.randint(3, random.randint(4, 9)),
                   wsaj + random.randint(3, random.randint(4, 9))))
wsaka = list(range(wsak - random.randint(3, random.randint(4, 9)),
                   wsak + random.randint(3, random.randint(4, 9))))
wsbha = list(range(wsbh - random.randint(3, random.randint(4, 9)),
                   wsbh + random.randint(3, random.randint(4, 9))))
wsbja = list(range(wsbj - random.randint(3, random.randint(4, 9)),
                   wsbj + random.randint(3, random.randint(4, 9))))
wsbka = list(range(wsbk - random.randint(3, random.randint(4, 9)),
                   wsbk + random.randint(3, random.randint(4, 9))))
wscha = list(range(wsch - random.randint(3, random.randint(4, 9)),
                   wsch + random.randint(3, random.randint(4, 9))))
wscja = list(range(wscj - random.randint(3, random.randint(4, 9)),
                   wscj + random.randint(3, random.randint(4, 9))))
wscka = list(range(wsck - random.randint(3, random.randint(4, 9)),
                   wsck + random.randint(3, random.randint(4, 9))))
wsdha = list(range(wsdh - random.randint(3, random.randint(4, 9)),
                   wsdh + random.randint(3, random.randint(4, 9))))
wsdja = list(range(wsdj - random.randint(3, random.randint(4, 9)),
                   wsdj + random.randint(3, random.randint(4, 9))))
wsdka = list(range(wsdk - random.randint(3, random.randint(4, 9)),
                   wsdk + random.randint(3, random.randint(4, 9))))

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

workbook.save('8西西1-18-3.xls')
