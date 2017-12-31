#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: regular.py
@time: 2017/12/30 20:48
"""
import re

phone = "2004-959-559 # 这是一个电话号码"

num = re.sub(r'#.*$', '', phone)
print("电话号码：", num)
