# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-1
.......time: 2018/07/26 21:38:21
Created with Visual Studio Code.
description: 类和调用类
"""


class Students(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


class TwoStudent(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


if __name__ == '__main__':
    zs = Students('张三', 99)
    ls = TwoStudent('李四', 89)
    zs.print_score()
    ls.print_score()
    print(zs.name)
    # print(ls.__name)  # 私有变量无法访问