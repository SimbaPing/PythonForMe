# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 22:35:52
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 22:42:06
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，
# 共经过多少米？第10次反弹多高？

Sn = 100.0
Hn = Sn / 2

for n in range(2, 11):
    Sn += 2 * Hn
    Hn /= 2

print 'Total of road is %f' % Sn
print 'The tenth is %f meter' % Hn
# 设计计算公式，开始先确定几个有确切数字的值
# 然后写一些计算公式
