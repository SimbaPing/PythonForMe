# -*- coding:utf-8 -*-
# 数字比较。
if __name__ == '__main__':
    i = int(raw_input('first> '))  # 输入数字一定要加int
    j = int(raw_input('second> '))
    if i > j:
        print '%d 大于 %d' % (i, j)
    elif i == j:
        print '%d 等于 %d' % (i, j)
    elif i < j:
        print '%d 小于 %d' % (i, j)
    else:
        print 'Shit'
