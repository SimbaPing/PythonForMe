#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: rh3.py
@Time: 2018/5/26 23:20
"""

from requests_html import HTMLSession
import requests

session = HTMLSession()

url = "http://www.99mm.me/qingchun/2833.html"
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/63.0.3239.26 '
                  r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}
data = {'name': 'pin', 'password': 'xxxxxxxx'}
r = requests.get(url, data=data, headers=headers)
# print(r)
r.encoding = 'gbk'
r = session.get(url)

print(r.html.links)


