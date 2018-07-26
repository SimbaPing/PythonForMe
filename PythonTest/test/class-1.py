#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-1
.......date: 2018/7/25 9:38
created with IntelliJ IDEA
description:
"""


class Fib(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


if __name__ == '__main__':
    end = []
    for i in Fib(10, 20):
        end.append(i)
    print(end)
