# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-08 20:31:07

import urllib.request
from bs4 import BeautifulSoup

res = 'http://jandan.net/ooxx'
html = BeautifulSoup(res, "html.parser")
for index, each in enumerate(html.select('#comments img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(urllib.requests.get(each.attrs['src'], stream=True).content)
