# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-28 21:46:21
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-28 21:54:29
# 输入3个数a,b,c，按大小顺序输出。
if __name__ == '__main__':
    n1 = int(raw_input('n1 = :\n'))
    n2 = int(raw_input('n2 = :\n'))
    n3 = int(raw_input('n3 = :\n'))

    def swap(p1, p2):
        return p2, p1
    # 这尼玛竟然要三个if循环
    if n1 > n2:
        n1, n2 = swap(n1, n2)
    if n1 > n3:
        n1, n3 = swap(n1, n3)
    if n2 > n3:
        n2, n3 = swap(n2, n3)

    print n1, n2, n3
