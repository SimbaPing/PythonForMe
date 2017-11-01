# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-26 19:39:01
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-26 19:43:51

# 使用lambda来创建匿名函数。
# 这个还不懂
MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a, b)
    print 'The lower one is %d' % MINIMUM(a, b)
