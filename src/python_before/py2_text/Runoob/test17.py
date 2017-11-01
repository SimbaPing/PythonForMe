# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 21:07:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 22:23:54

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string  # 用到了这个模块
s = raw_input('input a string:\n')
letters, space, digit, others = 0, 0, 0, 0  # 有数学计算的时候，将所用到的参数设为0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d, space = %d, digit = %d, others = %d' % (letters, space, digit, others)
