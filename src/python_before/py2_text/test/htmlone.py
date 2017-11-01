# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-16 18:48:14
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-16 18:55:36
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

# 添加一个解析器
soup = BeautifulSoup(html, 'html5lib')
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.body)

# 从文档中找到所有<a>标签的内容
for link in soup.find_all('a'):
    print(link.get('href'))


# 从文档中找到所有文字内容
print(soup.get_text())
