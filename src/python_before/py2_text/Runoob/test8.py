# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 21:29:35
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 21:59:40

# 输出乘法口诀
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print  '%d * %d = % -3d' % (i, j, result)  # 这个间隔还不懂
    print ''  # i 每当运行完一个数字就打印一个空行
