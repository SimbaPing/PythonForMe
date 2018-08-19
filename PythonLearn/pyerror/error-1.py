#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: error-1
.......date: 2018/8/19 21:20
created with IntelliJ IDEA
description:
"""


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常")  # type 结果
except IOError:
    print("Error: 没有找到文件或读取文件失败！")
else:
    print("内容写入文件成功")  # 结果输出这个
    fh.close()

try:
    fm = open("testfile1", "w")
    fm.write("第一个测试软件")
finally:
    print("ERROR，发生了异常。")


def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n", Argument)

temp_convert("xyz")


def mye(level):
    if level < 1:
        raise Exception("Invalid level")

try:
    mye(0)
except Exception as err:
    print(1, err)
else:
    print(2)


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.args)