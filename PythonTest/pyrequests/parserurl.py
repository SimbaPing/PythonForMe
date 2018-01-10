#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: parserurl.py
@time: 2018/1/9 23:46
"""

from bs4 import BeautifulSoup
import requests
import urllib.request
import re

url = 'http://www.meizitu.com/a/5568.html'
# url = 'http://httpbin.org/post'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/63.0.3239.26 '
                  r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}
data = {'name': 'ping', 'password': 'xxxxxxxx'}
r = requests.get(url, data=data, headers=headers)  # 给网页加上表单和模拟浏览器
r.encoding = 'gbk'  # 不会出现中文乱码
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
# 以上 OK
# print(soup.title)
# print(soup.find_all('img'))

ss = re.compile(r"http://*.jpg")
print(ss.findall('nihao'))


# for i in s:
#     print(i)
