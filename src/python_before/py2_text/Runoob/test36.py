# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 17:13:56
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 17:30:23

# 求100之内的素数。
lower = int(input('lower>'))
upper = int(input('upper>'))

for num in range(lower, upper + 1):  # range()取值范围自己定
    if num > 1:  # 素数大于1
        for i in range(2, num):  #　不能除１和他自己　这个完美
            if num % i == 0:　　# 余数等于0就说明成功
                break
        else:  # 从这个地方开始else
            print num  # 打印出num
