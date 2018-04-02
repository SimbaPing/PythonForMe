#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: requestshtml_jiandan.py
@Time: 2018/4/1 16:31
"""
# 爬煎蛋又失败了，爬出来的是个 1X1 的小图，哈哈哈哈
from requests_html import HTMLSession
from requests_html import HTML

url = 'http://jandan.net/ooxx/page-67#comments'
session = HTMLSession()
r = session.get(url)

about = r.html.find('.commentlist', first=all)
print(about.find('img'))
