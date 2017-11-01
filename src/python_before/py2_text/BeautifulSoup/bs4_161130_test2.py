# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-08 17:22:03

from bs4 import BeautifulSoup

html_doc = """
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

soup = BeautifulSoup(html_doc, 'html.parser')
# print soup.prettify()  # 按照标准的缩进格式输出
print soup.title  # <title>The Dormouse's story</title>
print soup.title.name  # title
print soup.title.string  # The Dormouse's story
print soup.title.parent.name  # 父名字 head
print soup.p  # <p class="title"><b>The Dormouse's story</b></p>
print soup.p['class']  # [u'title']
print soup.a  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print soup.find_all('a')  # 返回一个列表 全部<a>
print soup.find(id="link3")  # 返回这个id的标签

# 在文档中找出所有<a>标签的链接：
for link in soup.find_all('a'):  # find_all
    print link.get('href')  # get
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

# 从文档中获取所有文字内容：
print soup.get_text()  # 如题，那么我获得某条内容怎么办呢
