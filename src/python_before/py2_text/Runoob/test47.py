# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-26 19:31:03
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-26 19:33:48


# 两个变量值互换

#　这个例子貌似很经典
def exchange(a, b):
    a, b = b, a
    return (a, b)

if __name__ == '__main__':
    x = 10
    y = 20
    print 'x = %d, y = %d' % (x, y)
    x, y = exchange(x, y)
    print 'x = %d, y = %d' % (x, y)
