# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 13:25:19
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 19:03:57

# 打印水仙花数
for n in range(100, 1000):
    i = n / 100
    j = n / 10 % 10  # / 得到前两位数 %得到后一位数
    k = n % 10  # 得到余数 就是最后一位数
    if n == i ** 3 + j ** 3 + k ** 3:
        print n
