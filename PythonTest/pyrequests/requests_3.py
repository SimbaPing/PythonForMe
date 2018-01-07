#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: requests_3.py
@time: 2018/1/7 16:23
"""

from bs4 import BeautifulSoup
import requests
import urllib.request
import re

url = 'http://www.meizitu.com/a/5530.html'
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
urlurl = r.text
soup = BeautifulSoup(urlurl, 'html.parser')
# links = soup.find_all(id='picture')

reg = r'src="(*\.jpg)" pic_ext="jpeg"'
imgre = re.compile(reg)
imglist = re.findall(imgre, soup)
# for link in links:
#     print(link.name)
#
