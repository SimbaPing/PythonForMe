#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-3
.......date: 2018/7/28 22:16
created with IntelliJ IDEA
description:
"""


class Student(object):
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    s = Student()
    s.name = "John"
    s.age = 15
