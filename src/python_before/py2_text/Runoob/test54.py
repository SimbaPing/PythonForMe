# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 19:46:43
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 19:50:35

# 取一个整数a从右端开始的4~7位。
if __name__ == '__main__':
    a = int(raw_input('> \n'))
    b = a >> 4
    c = ~ (~ 0 << 4)
    d = b & c
    print '%o\t%o' % (a, d)
