#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: meitu_1.py
@time: 2018/1/2 1:38
"""
import socket
import urllib.request
import http.cookiejar

import os


def getHtml(url):
    # 创建 cookie 容器
    cj = http.cookiejar.CookieJar()
    # 代理服务器
    proxy_handler = urllib.request.ProxyHandler({'http': '58.252.6.165:9000'})
    # 创建 opener，里面可以放多个参数，最常见 cookie 和 proxy
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
    # 给 urllib.request 安装 opener
    urllib.request.install_opener(opener)

    values = {'name': 'pin', 'password': 'xxxxxxxx'}
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/63.0.3239.26 '
                      r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection': 'keep-alive',
        'Referer': "http://www.meizitu.com/",
        'Cache-Control': 'max-age=31536000',
        'Content-Encoding': 'gzip',
        'Content-Length': '2007'
    }
    data = urllib.parse.urlencode(values).encode(encoding='utf-8')
    req = urllib.request.Request(url, data, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf8')  # 如果添加 decode('utf-8')，那么下面的就不好开展工作
    response.close()
    return html


if __name__ == '__main__':
    print("开始")
    os.chdir('mtpic')
    mturl = 'http://www.meizitu.com/'
    mhtml = getHtml(mturl)
    print("ii")
