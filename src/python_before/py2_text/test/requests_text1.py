# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-07 08:27:31
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-07 08:48:23

import requests

from

# 1、发送http请求
r = requests.get('http://httpbin.org/ip')  # r可以获得http请求的响应结果
print r
h = requests.post('http://httpbin.org/post', data={'name': 'leo'})  # 要发送post请求
print h

# 2、构造URL http://httpbin.org/get?key1=value1&key2=value2
d = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=d)
print r.url

# 3、http响应正文
r = requests.get('http://httpbin.org/ip')  # r可以获得http请求的响应结果
print r.text  # 获取响应的正文文本内容
