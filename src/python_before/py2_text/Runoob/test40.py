# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 18:22:21
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 18:37:30

# 将一个数组逆序输出。
if __name__ == '__main__':  # 意思就是直接开始运行
    a = [9, 6, 5, 4, 1]
    N = len(a)
    print a
    for i in range(len(a) / 2):  # i为a总长的一半
        a[i], a[N - i - 1] = a[N - i - 1], a[i]  # 公式有点复杂
    print a
