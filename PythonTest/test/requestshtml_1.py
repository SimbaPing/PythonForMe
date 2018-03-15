#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: requestshtml_1.py
@Time: 2018/2/28 15:58
"""

from requests_html import HTMLSession
from requests_html import HTML

session = HTMLSession()
r = session.get('https://python.org/')  # 请求链接
print(1)
print(r.html.links)  # 获取页面中所有的链接形成一个列表，我觉得应该叫字典
print(2)
print(r.html.absolute_links)  # 获取绝对形式的链接
print(3)
about = r.html.find('#about', first=True)
print(about.text)
print(4)
print(about.attrs)
print(5)
print(about.html)
print(6)
print(about.find('a'))
print(7)
print(about.absolute_links)
print(8)
print(r.html.search('Python is a {} language')[0])
# print(9)
# r = session.get('https://github.com/')
# sel = 'body > div.application-main > div.jumbotron.jumbotron-codelines > div > div > ' \
#       'div.col-md-7.text-center.text-md-left > p '
# print(r.html.find(sel, first=True).text)
print(10)
print(r.html.xpath('a'))
print(11)
# r = session.get('http://python-requests.org')
# r.html.render()
# print(r.html.search('Python 2 will retire in only {months} months!')['months'])
print(12)
doc = """<a href='https://httpbin.org'>"""
html = HTML(html=doc)
print(html.links)
print('end')
