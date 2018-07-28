#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-5
.......date: 2018/7/28 22:56
created with IntelliJ IDEA
description: 多重继承之拓扑排序
"""


class A(object):

    @staticmethod
    def foo():
        print('A foo')

    @staticmethod
    def bar():
        print('A bar')


class B(object):

    @staticmethod
    def foo():
        print('B foo')

    @staticmethod
    def bar():
        print('B bar')


class C1(A, B):
    pass


class C2(A, B):

    def bar(self):
        print('C2-bar')


class D(C1, C2):
    pass


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.foo()
    d.bar()
