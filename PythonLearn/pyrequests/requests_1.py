#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: requests_1.py
@time: 2018/1/2 10:20
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.meizitu.com/'
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
soup = BeautifulSoup(r.text, 'lxml')
imgList = soup.find('div', id='maincontent').find_all('a')
# print(imgList)
for a in imgList:
    title = a.get_text()
    href = a['href']
    print(title, href)



