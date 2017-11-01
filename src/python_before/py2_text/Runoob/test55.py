# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 19:53:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 20:04:05

# 学习使用按位取反~。
if __name__ == '__main__':
    a = 234
    b = ~a
    print 'The a \'s 1 complement is %d' % b
    a = ~a
    print 'The a \'s 2 complement is %d' % a

for i in range(0, 5) + range(2, 8) + range(3, 12) + [2, 2]:
    print ' ' * (40 - 2 * i - i // 2) + '*' * (4 * i + 1 + i)
