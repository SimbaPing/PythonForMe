#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with IntelliJ IDEA by Django on 2019/12/1 17:44
# print("Python Version {}".format(str(sys.version).replace('\n', '')))  # 获得版本号

# import sys

import requests
from bs4 import BeautifulSoup

url = 'http://kaijiang.500.com/shtml/dlt/07001.shtml'

headers = {'referer': 'http://kaijiang.500.com/shtml/dlt/07001.shtml', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

r = requests.get(url, headers=headers)
r.encoding = 'gbk'
# print(r.text)
# print(r.encoding)

soup = BeautifulSoup(r.text, 'lxml')
items = soup.find_all('li', class_='ball_red')
for link in items:
    print(link.string)
print(items)

