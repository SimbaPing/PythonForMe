#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: requestshtml_2.py
@Time: 2018/4/1 16:49
"""

# 这个网站应该也有防爬

from requests_html import HTMLSession
from requests_html import HTML

url = 'http://www.meizitu.com/a/5584.html'
session = HTMLSession()
r = session.get(url)
print(r.html.absolute_links)

about = r.html.find('#picture', first=True)
# print(about)
