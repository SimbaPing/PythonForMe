#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: end.py
@time: 2018/1/9 23:26
"""
import requests


def getHtml(urlurl):
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/63.0.3239.26 '
                      r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection': 'keep-alive'
    }  # 头
    data = {'name': 'ping', 'password': 'xxxxxxxx'}  # 表单
    r = requests.get(urlurl, data=data, headers=headers)  # 给网页加上表单和模拟浏览器
    r.encoding = 'gbk'  # 正常显示中文

    return r


if __name__ == '__main__':
    url = 'http://www.meizitu.com/a/5530.html'  # 一个妹子图的链接
    r = getHtml(url)
    print(r.text)
