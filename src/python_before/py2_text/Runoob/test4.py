# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 19:47:11
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 20:07:50

# 定义年月日
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

# 创建一个列表
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < month <= 12:
    sum = months[month - 1]  # 月之和
else:
    print 'data error'
sum += day  #总和等于　月之和加上日之和

# 判断是不是闰年，闰年加一天
leap = 0
if (year % 400 == 0) or (year % 4 == 0) or (year % 100 != 0):
    leap = 1
if (leap == 1) and (month > 2):  # 闰年并且月份大于2
    sum += 1
print 'it is the %dth day.' % sum
