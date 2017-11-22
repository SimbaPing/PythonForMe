#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: IOfile.py
@time: 2017/11/21 16:51
"""

# 新建文件，然后在里面写东西，已经有了就覆盖创建，中文加上 encoding
with open("test.txt", "w", encoding="utf-8") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧啊！")

