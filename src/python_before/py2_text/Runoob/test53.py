# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 19:30:50
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 19:42:56

# 学习使用按位异或 ^
# 0^0=0; 0^1=1; 1^0=1; 1^1=0
if __name__ == '__main__':
    a = 077
    b = a ^ 3
    print 'The a ^ 3 = %d' % b
    b ^= 7
    print 'The a ^ b = %d' % b
