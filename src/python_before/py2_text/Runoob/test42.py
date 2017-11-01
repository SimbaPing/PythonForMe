# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-25 22:59:43
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-25 23:06:48

# 学习使用auto定义变量的用法
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):  # 原来是从这里开始运行的
    print 'The num = %d' % num
    num += 1
    autofunc()  # 既然已经定义好了，那这就是局部变量，全局变量也影响不了
