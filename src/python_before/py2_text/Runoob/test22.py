# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-22 10:00:21
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-22 10:11:30
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != ord('x')) & (k != ord('x')) & (k != ord('z')):
                    print 'order is a -- %s\t b -- %s\t c -- %s' % (chr(i), chr(j), chr(k))
