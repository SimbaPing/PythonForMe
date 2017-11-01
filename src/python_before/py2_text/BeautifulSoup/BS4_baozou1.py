# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-11-26 12:18:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-06 22:30:50

from bs4 import BeautifulSoup
import os
import sys
import urllib2
import time
import random
import urllib
import requests
# 创建文件夹
path = os.getcwd()  # 获取当前路径
new_path = os.path.join(path, u'暴走漫画')  # 在当前路径中创建文件夹
if not os.path.isdir(new_path):
    os.mkdir(new_path)


url = 'http://baozoumanhua.com/baoman'
values = {'name' : 'Michael Foord',
          'location' : 'pythontab',
          'language' : 'Python' }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
data = urllib.urlencode(values)
resp = urllib2.Request(url, data, headers)
try:
    content = urlopen(resq)
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
soup = BeautifulSoup(content, 'lxml')
my_girl = soup.find_all('img', class_="lazy")
for girl in my_girl:
    link = girl.get('data-url')
    flink = link
    print flink
    content2 = urllib2.urlopen(flink).read()
    print content2
