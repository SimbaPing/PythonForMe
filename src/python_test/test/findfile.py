#!/usr/bin/env python
# encoding: utf-8
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: findfile.py
@time: 2017/11/18 22:52
@desc:
"""

import os
import os.path

l = []
def get_py(path, l):
    fileList = os.listdir(path)
    for filename in fileList:
        pathTmp = os.path.join(path, filename)
        if os.path.isdir(pathTmp):
            get_py(pathTmp, l)
        elif filename[-3:].upper() == '.PY':
            l.append(pathTmp)
path = input('请输入路径： ').strip()
get_py(path, l)
print('在 %s 目录及其子目录找到 %d 个文件 \n 分别为：\n'%(path,len(l))
for filepath in l:
    print(filepath + '\n')