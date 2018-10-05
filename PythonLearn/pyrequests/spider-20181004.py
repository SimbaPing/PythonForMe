#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/4 16:28
Filename: spider-20181004.py
Contact: uppjs@qq.com
Description: 
"""

from bs4 import BeautifulSoup
import requests

url = 'https://alpha.wallhaven.cc/latest'
# url = 'http://httpbin.org/post'
headers = {
    'User-Agent': r'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/69.0.3497.92 Safari/537.36',
    'Connection': 'keep-alive',
    'referer': 'https://alpha.wallhaven.cc/',
    'cookie': '__cfduid=d5224f2c93e86978f2cdf4b70286f802a1536932309; '
              '_pk_ref.1.1f04=%5B%22%22%2C%22%22%2C1538643704%2C%22https%3A%2F%2Fwallhalla.com%2Fwallpaper'
              '%2FLbGzeDd7TPMN%22%5D; _pk_ses.1.1f04=*; '
              'wallhaven_session=eyJpdiI6Ilh4cEtIc1wvSkFkaU5ibFNUdGd3bGtzSDJaeFwvemJvaVNaTWR5OW0yY3d0WT0iLCJ2YWx1ZSI6Im1IdnlDKzg5R2dhM1RMbDVTQlpSaDA0WjZmWVlYaVpkWTFxM2JBNnpFZEZ6MFc5R2h3d21ydVhUWWRidzlUMzkzZlF5YncwaFJqQVo3Y3h6VVpXWEtBPT0iLCJtYWMiOiI1OWM3MTM2YWU2NjdiMmY0YjhmYjkwNGE1ODM1YTFjMzRiMDg2YjM0ZmQwNzYzYTk3OGM3ZThkNjVlOTdiODBiIn0%3D; _pk_id.1.1f04=9cfe5030d2039346.1536932333.9.1538643710.1538643704. '


}
r = requests.get(url, headers=headers)  # 给网页加上表单和模拟浏览器
r.encoding = 'br'
# 以上 OK
# print(r.text)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title)
