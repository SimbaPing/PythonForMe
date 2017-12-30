#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: spider_getFile.py
@time: 2017 2017/12/30 16:29
"""

import os
import os.path


# 这个的目的是创建文件夹，并将文件填入文件夹内
# 1. 目录，文件夹
def folder():  # 把东西放在这个里面就不会直接运行了
    os.chdir('C:/Users/pjs/Github/PythonForMe/python_test/pyspiders/two')  # 打开这个路径
    os.mkdir('three')  # 不写路径，默认当前路径创建文件夹，当文件已经创建就会报错
    os.getcwd()  # 获取当前目录
    os.rmdir('')  # 删除目录文件夹


# 2. 文件 操作完后要 close
def file():
    # 2.1 已有文件操作
    f = open('one.txt', encoding='utf8')  # 打开文件，中文要转码，如果文件不存在就返回错误
    print(f.readline())  # 打印一行
    print(f.read())  # 打印剩下的所有数据，文件大时不要用
    print(f.name)  # 文件名
    print(f.mode)  # 文件的模式读还是写
    print(f.closed)  # 如果文件被关闭了返回 true，否则返回 false
    # 2.2 创建文件
    wf = open('two.txt', 'w', encoding='utf8')  # 'w' 写入，也就是创建文件夹，如果已经存在，将擦除后重建这个文件
    wf.write('这里是内容')  # 写入字符串
    wf.writelines('')  # 写入多行
    # 2.3 同样是对文件进行操作，不用写 close，
    with open('three.txt', 'w', encoding='utf8') as ff:
        print(ff.name)
    # 2.4 删除文件
    os.remove('three.txt')
    os.remove('two.txt')
    # 2.5 重命名文件
    os.rename('old', 'new')

