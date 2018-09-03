#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: reverse-integer
.......date: 2018/9/3 23:12
created with IntelliJ IDEA
description:
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        a = list(str(x))
        b = []
        for i in range(0, len(a)):
            b.append(a[len(a) - i - 1])
        c = list(map(int, b))
        d = c[0] * 100 + c[1] * 10 + c[2] * 1
        print(d)
    elif x == 0:
        print(x)
    elif x < 0:
        x = abs(x)
        a = list(str(x))
        b = []
        for i in range(0, len(a)):
            b.append(a[len(a) - i - 1])
        c = list(map(int, b))
        d = c[0] * 100 + c[1] * 10 + c[2] * 1
        print(-d)


if __name__ == '__main__':
    reverse(x=-120)
