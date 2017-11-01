# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 16:53:00
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 16:57:17

# 按逗号分隔列表。
L = [1, 2, 3, 4, 5]
print L
print str(L)
print '-'.join(str(L))
sl = '*'.join(str(n) for n in L)
print sl
