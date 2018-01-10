#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: pyjson.py
@time: 2018/1/10 10:01
"""

import json

data = {
    'no': 1,
    'name': 'uppjs',
    'url': 'http://nameping.xyz'
}

json_str = json.dumps(data)
print('Python 原始数据：', repr(data))
print('JSON 对象：', json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']", data2['name'])
print("data2['url']", data2['url'])
