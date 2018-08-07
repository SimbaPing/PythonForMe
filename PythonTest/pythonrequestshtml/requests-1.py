#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: requests-1
.......date: 2018/8/6 23:55
created with IntelliJ IDEA
description:
"""
import requests
from requests_html import HTML
r = requests.get('http://baidu.com', auth=('user', 'pass'))
print(r.status_code)

doc = """<a href='http://baidu.com/'>"""
html = HTML(html=doc)
print(html.links)