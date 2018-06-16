#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: tt.py
@Time: 2018/6/6 17:04
"""

import xlrd

data = xlrd.open_workbook('C:\\Users\\pjs\\Github\\learnpython\\PythonTest\\taihe\\aa.xls')

table = data.sheets()[0]

nrows = table.nrows

print(nrows)

aa = table.row_values(5)[2:3]

print(aa + 3)
