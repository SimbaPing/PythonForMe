# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 10:11:46
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 10:36:54
from sys import stdout  # 跟print差不多，要打印但是不打印
for i in range(4):  # 共有四行
    for j in range(2 - i + 1):
        stdout.write(' ')  # 依次打印空格
    for k in range(2 * i + 1):
        stdout.write('*')  # 紧随其后 打印 *
    print  # 　打印最开始的for 将这四行B打印出来
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print
