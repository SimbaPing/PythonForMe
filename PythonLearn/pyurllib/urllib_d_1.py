#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: urllib_d_1.py
@time: 2018/1/18 22:33
"""

import urllib.request

url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url)
print(response.getcode())
print(response)

