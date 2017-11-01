# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-30 12:08:37
# @Last Modified by:   Administrator
# @Last Modified time: 2016-11-26 12:16:39

import urllib2
import re
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
soup = BeautifulSoup(html_doc, "lxml")  # 用 lxml 解析
# soup.标签.标签里面的元素
print soup.title  # <title>The Dormouse's story</title>
print soup.title.name  # title
print soup.title.string  # The Dormouse's story
print soup.p  # <p class="title"><b>The Dormouse's story</b></p>
print soup.a  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print soup.find_all('a')  # 返回列表 全部<a>打印
print soup.find(id='link3')  # 返回标签 打印拥有这个元素的标签
print soup.get_text()  # 只打印网页显示部分
print soup.find_all('title')
print soup.find_all(id=True)  # 返回列表 打印全部
print soup.find_all("a", attrs={"class": "sister"})  # 返回列表 打印拥有这个属性的标签
print soup.find_all(text="Elsie")  # 打印网页显示内容
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])  # 他会自动按照正确顺序打印
print soup.find_all("a", limit=2)  # 界限 打印前两个
print soup.select("p.title")  # 返回列表 通过css查找
