# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 10:38:31
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 16:44:32

# 请输入星期几的第一个字母来判断一下是星期几，
# 如果第一个字母一样，则继续判断第二个字母

# 条件语句 一条一条的向下延伸
letter = raw_input("please input:")
if letter == 'S':
    print 'Place input second letter:'
    letter = raw_input('please input:')
    if letter == 'a':
        print 'Saturday'
    elif letter == 'u':
        print 'Sunday'
    else:
        print 'data error'

elif letter == 'F':
    print 'Friday'
elif letter == 'M':
    print 'Monday'
elif letter == 'T':
    print 'Place input second letter'
    letter = raw_input('please input:')

    if letter == 'u':
        print 'Tuesday'
    elif letter == 'h':
        print 'Thursday'
    else:
        print 'data error'
elif letter == 'W':
    print 'Wednesday'
else:
    print 'data error'
