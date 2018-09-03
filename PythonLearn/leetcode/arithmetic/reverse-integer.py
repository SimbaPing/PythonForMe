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


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            a = list(str(x))
            b = list
            for i in range(0, len(a)):
                b.append(a[len(a) - i - 1])

        elif x = 0:
            return 0
        elif x < 0:
            return


if __name__ == '__main__':
    x = 123
