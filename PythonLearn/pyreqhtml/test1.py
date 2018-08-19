#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: test1.py
@Time: 2018/3/15 15:24
"""


from requests_html import HTMLSession
from requests_html import HTML


url = 'http://www.meizitu.com/'

session = HTMLSession()
r = session.get(url)
img = r.html.find('img')
for src in img:
    print(src)

