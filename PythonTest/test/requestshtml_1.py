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
