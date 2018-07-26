# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-1
.......time: 2018/07/26 21:38:21
Created with Visual Studio Code.
description:
"""


class Students(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


if __name__ == '__main__':
    zs = Students('张三', 99)
    ls = Students('李四', 89)
    zs.print_score()
    ls.print_score()
