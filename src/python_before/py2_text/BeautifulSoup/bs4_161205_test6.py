# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-05 22:52:56
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-06 21:21:11

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
from bs4 import BeautifulSoup
from bs4 import Comment
import bs4, urllib2, urllib, re
# 修改文档树

# 修改tag的名称和属性
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
print tag
del tag['class']
del tag['id']
print tag
# 修改 .string
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'lxml')
tag = soup.a
tag.string = "New link text."
print tag
# append()
soup = BeautifulSoup("<a>Foo</a>", 'lxml')
soup.a.append('Bar')
print soup
print soup.a.contents
# Navigablestring() & .nex_tag()
soup = BeautifulSoup('<b></b>', 'lxml')
tag = soup.b
tag.append('Hello')
new_string = u' there'
tag.append(new_string)
print tag
print tag.contents
# 创建一段注释
new_comment = soup.new_string('Nice to see you.', Comment)
tag.append(new_comment)
print tag

print '-' * 66

# 创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag()
soup = BeautifulSoup('<b></b>', 'lxml')
original_tag = soup.b
new_tag = soup.new_tag('a', href='http://www.example.com')
original_tag.append(new_tag)  # 在标签之中又添加了一个标签
print original_tag
new_tag.string = 'Link text.'  # 增加字符串
print original_tag
# insert
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'lxml')
tag = soup.a
tag.insert(1, "but did not endorse ")  # 在第一段字符串中添加这个
print tag
# insert_before()
soup = BeautifulSoup('<b>stop</b>', 'lxml')
tag = soup.new_tag('i')  # 新标签名字<i>
tag.string = "Don't"  #  新标签字符串内容
soup.b.string.insert_before(tag)  # 在前面重新添加一个tag标签
print soup.b
# & insert_after()
soup.b.i.insert_after(soup.new_string(' ever '))
print soup.b
print soup.b.contents
# clear() tag.clear()方法移除当前tag的内容
soup = BeautifulSoup(markup, 'lxml')
tag = soup.a
tag.clear()  # 到底移除了啥
print tag
# extract() ??
# decompose()
# replace_with()
# warp()
# unwarp()


print '+' * 66

# 输出
# 格式化输出
# prettify()方法
soup = BeautifulSoup(markup, 'lxml')
print soup.prettify()
print soup.a.prettify()
# 压缩输出
# Unicode()方法 & str()
print str(soup)  # 返回的是utf-8
print unicode(soup.a)
# 输出格式
soup = BeautifulSoup('&ldquo;Dammit!&rdquo; he said.', 'lxml')
print unicode(soup)
# get_text()
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'lxml')
print soup.get_text()  # 提取字符串 全部
print soup.i.get_text()  # 提取指定字符串
print soup.get_text('|')  # 不同标签字符串用这个隔开
print soup.get_text('|', strip=True)  # 去除前后空白
print [text for text in soup.stripped_strings]  # 生成器

print '-' * 55

#指定文档解析器
jiexiqi = ['xml', 'lxml', 'html5lib', 'html.parser']
for jiexi in jiexiqi:
    print BeautifulSoup('<a></p>', jiexi)
# 编码
markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
soup = BeautifulSoup(markup, 'lxml')
print soup.h1
print soup.h1.string
print soup.original_encoding  # 记录了自动识别编码的结果
markup = b"<h1>\xed\xe5\xec\xf9</h1>"
soup = BeautifulSoup(markup, 'lxml')
print soup.h1
print soup.original_encoding
# 通过传入 from_encoding参数来指定编码方式
soup = BeautifulSoup(markup, 'lxml', from_encoding='iso-8859-8')
print soup.h1
print soup.original_encoding
 # 文档不会尝试这种编码exclude_encodings
soup = BeautifulSoup(markup, 'lxml', exclude_encodings=["ISO-8859-7"])
print soup.h1
print soup.original_encoding
# 调用任意节点的 encode()方法

