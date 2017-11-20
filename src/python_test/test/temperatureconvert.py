#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: temperatureconvert.py
@time: 2017/11/21 1:32
other： 摄氏度转为华氏度, 以后可以加上一个选择，华氏摄氏选择进行转换
"""

celsius = float(input('输入摄氏温度：'))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f' % (celsius, fahrenheit))
