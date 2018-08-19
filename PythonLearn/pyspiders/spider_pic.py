#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: spider_pic.py
@time: 2017 2017/12/30 9:12
"""
import urllib.request
import http.cookiejar
import re, os
from bs4 import BeautifulSoup


def getHtml(url):
    # 创建 cookie 容器
    cj = http.cookiejar.CookieJar()
    # 代理服务器
    proxy_handler = urllib.request.ProxyHandler({'http': '103.87.16.2:80'})
    # 创建 opener，里面可以放多个参数，最常见 cookie 和 proxy
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
    # 给 urllib.request 安装 opener
    urllib.request.install_opener(opener)

    values = {'name': 'pin', 'password': 'xxxxxxxx'}
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 '
        r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
        r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection': 'keep-alive'
    }
    data = urllib.parse.urlencode(values).encode(encoding='utf-8')
    req = urllib.request.Request(url, data, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf8')  # 如果添加 decode('utf-8')，那么下面的就不好开展工作
    return html


def getImg(html):  # 转成 byte 它才肯干活
    reg = r'src="(.jpg)"'
    imgre = re.compile(reg, html)
    imglist = re.findall(imgre, html)
    return imglist

if __name__ == '__main__' :
    os.chdir('pic')
    inurl = 'http://jiandan.net/ooxx/page-425#comments'  # 初始网址
    inhtml = getHtml(inurl)  # 网站源码已经被解析出来了
    # print(inhtml)
    inimg = getImg(inhtml)  # imglist
    print(inimg)
    imgNum = 0
    for i in inimg:
        f = open("pic/" + str(imgNum) + ".jpg", 'wb')
        f.write((urllib.request.urlopen(i)).read())
        f.close()
        imgNum += 1
