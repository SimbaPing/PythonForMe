#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: jsontest.py
@Time: 2018/3/9 3:17
"""
'''
json.dumps(): 对 json 进行编码，对应 PHP 的 json_encode()
json.loads(): 对 json 进行解码，对应 PHP 的 json_decode()
'''

import json

test1 = {'a': 1, 'b': 2}
test2 = ['a', 1, 'b', 2]

test1_json = json.dumps(test1)
test2_json = json.dumps(test2)

print(test1_json)
print(test2_json)

print('=' * 20)

print(json.loads(test1_json))
print(json.loads(test2_json))
