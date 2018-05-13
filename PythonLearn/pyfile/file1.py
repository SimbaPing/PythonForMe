#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: file1.py
@Time: 2018/5/13 0:05
"""

import os
from os import path

filename = 'C:/Users/pjs/Github/name.txt'

if not os.path.exists(filename):
    os.system(r"touch {}".format(path))
