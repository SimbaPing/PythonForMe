# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-13 20:51:07
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-13 21:34:06


def displayNumType(num):
    print num, 'is',
    if isinstance(num, zifu):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

zifu = int, long, float, complex
displayNumType(-69)
displayNumType(999999999999)
displayNumType(98.6)
displayNumType(-5.32 + 1.5j)
displayNumType('xxx')
