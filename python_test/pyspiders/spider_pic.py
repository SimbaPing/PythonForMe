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
import re
from bs4 import BeautifulSoup


def getHtml(url):
    # 创建 cookie 容器
    cj = http.cookiejar.CookieJar()
    # 代理服务器
    proxy_handler = urllib.request.ProxyHandler({'http': '203.58.117.34:80'})
    # 创建 opener，里面可以放多个参数，最常见 cookie 和 proxy
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
    # 给 urllib.request 安装 opener
    urllib.request.install_opener(opener)

    values = {'name': 'pin', 'password': 'xxxxxxxx'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400',
        'Connection': 'keep-alive',
        'Host': 'jandan.net',
        'Referer': 'http://jandan.net/duan',
        'Accept-Language': 'zh-CN, zh; q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Upgrade-Insecure-Requests': '1'
    }
    data = urllib.parse.urlencode(values).encode(encoding='utf-8')
    req = urllib.request.Request(url, data, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def getImg(html):
    reg = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist


def getPic(img):
    imgName = 0
    f = open("pic/"+str(imgName)+".jpg", 'wb')
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName += 1

if __name__ == '__main__' :
    inurl = 'http://jandan.net/'
    inhtml = getHtml(inurl)
    print(inhtml)
    # inimg = getImg(inhtml)
    # out = getPic(inimg)
