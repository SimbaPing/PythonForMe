# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-30 21:27:45


def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % \
                (num, count)
            break
        count -= 1
    else:
        print num, "is prime"

for eachNum in range(10, 21):
    showMaxFactor(eachNum)
