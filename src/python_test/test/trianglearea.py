#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: trianglearea.py
@time: 2017/11/21 1:19
other：计算三角形的面积，有时候三个随机数不一定能组成三角形，以后需要加一个报错机制
"""

a = float(input('输入三角形的第一个边长: '))
b = float(input('输入三角形的第二个边长: '))
c = float(input('输入三角形的第三个边长: '))

s = (a + b + c) / 2  # 半周长
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # 这个计算的公式没听说过
print('三角形的面积为 %0.2f' % area)  # %0.2f 是浮点数精确到小数点后两位
