#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-4
.......date: 2018/7/28 22:24
created with IntelliJ IDEA
description:
"""


class Student(object):

    @property
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


if __name__ == '__main__':
    s = Student()
    s.set_score(60)
    s.get_score()
