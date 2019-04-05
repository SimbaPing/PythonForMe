#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with IntelliJ IDEA by Django on 2019/3/19 21:32

import requests
from bs4 import BeautifulSoup
import re

url = 'http://pic.xxx55tp.com/images/jlkaxklxkj/4887964/002.jpg'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
}

html = requests.get(url=url, stream=True)
with open('selenium.jpg', 'wb') as file:
    for data in html.iter_content(128):
        file.write(data)

print(requests.status_codes)
