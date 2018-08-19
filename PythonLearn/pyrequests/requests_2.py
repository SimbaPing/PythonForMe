#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: requests_2.py
@time: 2018/1/2 12:33
"""

# 这个利用了我不会的 lxml，返回逐行打印的链接，我很喜欢，但是不懂
import requests
from lxml import html


# 获取主页列表
def getPage():
    baseUrl = 'http://www.mzitu.com/'
    selector = html.fromstring(requests.get(baseUrl).content)

    urls = []
    for i in selector.xpath('//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    return urls


if __name__ == '__main__':
    urls = getPage()
    for url in urls:
        print(url)
