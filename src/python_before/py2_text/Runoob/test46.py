# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-26 12:45:17
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-26 12:58:57

# 求输入数字的平方，如果平方运算后小于 50 则退出。

TRUE = 1
FALSE = 0  # 两个全局变量


def SQ(x):  # 定义公式x
    return x * x
print '如果输入的数字小于50， 程序将停止运行。'
again = 1
while again:  # 将循环进行到海枯石烂
    num = int(raw_input('> '))
    print '%d' % (SQ(num))  # 无论怎样都是要出结果
    if num >= 50:
        again = TRUE
    else:
        again = FALSE
