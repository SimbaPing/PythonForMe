# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-02 23:02:17
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-04 11:38:28

from bs4 import BeautifulSoup

# 遍历文档树
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
soup = BeautifulSoup(html_doc, 'html.parser')  # html.parser用来解析HTML的模块

# tag 的名字
print soup.head  # 返回<head>标签
print soup.title  # 返回<title>标签
print soup.body.b  # 返回标签中的标签
print soup.a  # 返回第一个找到的标签

# find_all 返回一个列表 将标签
print soup.find_all('a')

# .contents tag属性，可以将tag的子节点以列表的方式输出
# 字符串没有.contents 属性，因为字符串没有子节点
print soup.head.contents  # 返回列表 head之中的内容，不包括head
print soup.title.contents  # u"" 是Unicode字符串
print len(soup.contents)
head_tag = soup.head
print head_tag
print head_tag.contents
title_tag = head_tag.contents[0]
print title_tag
print title_tag.contents

# 通过tag的.children 生成器可以对tag的子节点进行循环
# 有点不懂
for child in title_tag.children:
    print child
print len(list(soup.children))  # 2

# .descendants属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print child
print len(list(soup.descendants))  # 27

# .string 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
print title_tag.string  # 只有一个节点 打印该字符串
print soup.html.string  # 有多个，打印None

# .strings 和 stripped_strings
# 多个字符串 可以用.strings来循环获取
for string in soup.strings:  # 支持空格打印
    print repr(string)  # repr 标准字符串
for string in soup.stripped_strings:  # 去除多余的空白内容
    print repr(string)

# .parent 属性来获取某个元素的父节点
# 顶层节点回复None
title_tag = soup.title
print title_tag.parent

# .parents
# 递归得到所有父辈节点
link = soup.a
print link
for parent in link.parents:
    if parent is None:
        print parent
    else:
        print parent.name

# 兄弟节点 同一层的属于兄弟节点
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", "lxml")
print sibling_soup.prettify()

# .next_sibling 和 .previous_sibing 返回标签
print sibling_soup.b.next_sibling  # b以后的兄弟节点是什么 否则None
print sibling_soup.c.previous_sibling  # c以前的兄弟节点是什么

# 好几个<a>标签排着
link = soup.a
print link  # 打印第一个<a>
print link.next_sibling  # 是顿号  两个<a>之间
print link.next_sibling.next_sibling  # 这才是第二个<a>

print '-' * 66
# .next_siblings 和 .previous_siblings可以对当前节点的兄弟节点迭代输出
for sibling in soup.a.next_siblings:  # 兄弟节点 所以最后那一段字符串也有
    print repr(sibling)  # repr 纯碎的字符串
print '+' * 55
for sibling in soup.find(id="link3").previous_siblings:  # 倒着往回迭代
    print repr(sibling)

print '-' * 66
# .next_element 指向解析过程中下一个被解析的对象 字符串或tag
last_a_tag = soup.find("a", id="link3")  # 返回这个标签 找到<a>中 属性为link3的信息
print last_a_tag
print last_a_tag.next_sibling  # 本标签之后的字符串
print last_a_tag.next_element  # 属于本标签的字符串
# 和 .previous_element
print last_a_tag.previous_element  # 倒着往回找字符串
print last_a_tag.previous_element.next_element  # 呵呵

print '-' * 66
# .next_elements 和 .previous_elements  # 后面加s的都能迭代
for element in last_a_tag.next_elements:  # 将之后的字符串都迭代出来
    print repr(element)
