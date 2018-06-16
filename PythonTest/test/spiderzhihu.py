#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: spiderzhihu.py
@Time: 2018/6/4 19:09
"""
import http.cookiejar
import urllib.request
import urllib.parse

url = 'https://www.zhihu.com/question/279601094/answer/409278878' \

cj = http.cookiejar.CookieJar()
# 代理服务器
proxy_handler = urllib.request.ProxyHandler({'http': '103.87.16.2:80'})
# 创建 opener，里面可以放多个参数，最常见 cookie 和 proxy
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
# 给 urllib.request 安装 opener
urllib.request.install_opener(opener)

# values = {'username': 'fpsping@163.com', 'password': 'pjs1222'}
values = {'username': 'xxx', 'password': 'xxx'}
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 '
                  r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}
data = urllib.parse.urlencode(values).encode(encoding='utf8')
req = urllib.request.Request(url, data, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf8')
print(html)
