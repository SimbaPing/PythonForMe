#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: table1.py
@Time: 2018/5/23 10:16
"""

# 将数据写入 Excel 表格中

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 编码格式
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  # 表格名称

a = 16
# 第1种，写入数据位置及内容
booksheet.write(0, 0, 34)
booksheet.write(0, 1, 38)
booksheet.write(1, 0, 36)
booksheet.write(1, 1, 39)
booksheet.write(1, 2)
booksheet.write(1, 3, a)

# 第2种，数据包，借助 for in 完成写入
rowadata = [43, 56]
for i in range(len(rowadata)):
    booksheet.write(2, i, rowadata[i])
    print(rowadata[1])
# 保存为表格文件
# workbook.save('test_xlwt1.xls')

aa = [1, 6, 15, 12, 66, 13]

aa.sort()
print(aa)

