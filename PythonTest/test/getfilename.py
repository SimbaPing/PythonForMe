#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: getfilename.py
@Time: 2018/4/7 0:31
"""

import os

file_dir = 'C:/Users/pjs/GitHub'
for root, dirs, files in os.walk(file_dir):
    # print(root)
    # print(dirs)
    print(files)
