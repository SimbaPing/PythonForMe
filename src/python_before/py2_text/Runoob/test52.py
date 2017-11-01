# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 19:25:51
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 19:30:28

# 学习使用按位或 | 。
# 0|0=0; 0|1=1; 1|0=1; 1|1=1
# 不懂
if __name__ == '__main__':
    a = 077
    b = a | 3
    print 'a | b is %d' % b
    b |= 7
    print 'a | b is %d' % b

