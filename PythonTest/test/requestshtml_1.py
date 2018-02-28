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

session = HTMLSession()
r = session.get('https://python.org/')

print(r.html.links)
print(r.html.absolute_links)
about = r.html.find('#about', first=True)
print(about.text)
print(about.attrs)
print(about.html)
print(about.find('a'))
print(about.absolute_links)
print(r.html.search('Python is a {} language')[0])
r = session.get('https://github.com/')
sel = 'body > div.application-main > div.jumbotron.jumbotron-codelines > div > div > ' \
      'div.col-md-7.text-center.text-md-left > p '
print(r.html.find(sel, first=True).text)
print(r.html.xpath('a'))
