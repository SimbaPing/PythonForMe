#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: jiandan.py
@time: 2018/1/1 1:00
"""

import requests
from bs4 import BeautifulSoup

res = requests.get('http://jiandan.net/ooxx/')
html = BeautifulSoup(res.text, 'lxml')
print(html)
for index, each in enumerate(html.select('#comments img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(requests.get(each.attrs['src'], stream=True).content)
