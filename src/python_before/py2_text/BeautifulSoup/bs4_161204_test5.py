# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-12-04 11:39:00
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-06 18:46:36

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
soup = BeautifulSoup(html_doc, 'html.parser')

# 搜索文档树 find() find_all()  # 返回列表
print '+' * 66
# 过滤器：字符串 正则表达式 列表 True
# 字符串
print soup.find_all('b')
# 正则表达式
import re
for tag in soup.find_all(re.compile("^b")):  # 找到以b开头的标签
    print tag.name  # 只打印标签的name
for tag in soup.find_all(re.compile("t")):  # 找到带t的标签
    print tag.name
# 列表
print soup.find_all(["a", "b"])  # 找到带<a><b>标签的打印出来
# True 可以匹配任何值 但是不会返回字符串
for tag in soup.find_all(True):
    print tag.name  # 挨个打印 重复也打印

print '-' * 55
 # 方法 没有合适的过滤器，可以自己定义一个 方法只接受一个元素参数
def has_class_but_no_id(tag):  # 这个失败了，不知道什么原因
    return tag.has_attr("class") and not tag.has_attr("id")
print soup.find_all(has_class_but_no_id)
print '-' * 55
def not_lacie(href):  # href中没有lacie的
    return href and not re.compile("lacie").search(href)
print soup.find_all(href=not_lacie)
print '-' * 55
# 过滤前后都有文字的标签 擦，这个好复杂
from bs4 import NavigableString
def surrounded_by_strings(tag):
    return isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element, NavigableString)
for tag in soup.find_all(surrounded_by_strings):
    print tag.name

print '-' * 55
# find_all(name, attrs, recursive, string, **kwargs)
print soup.find_all('title')  # 返回列表 标签<title>
print soup.find_all('p', 'title')  # 返回列表 有title属性的<p>标签
print soup.find_all('a') # 返回列表 所有<a>
print soup.find_all(id='link2')  # 返回列表 含有link2属性的
print soup.find(string=re.compile('sisters'))  # 返回字符串 含有这个sisters

# name参数
print soup.find_all('title')
# keyword参数
print soup.find_all(id='link2')
print soup.find_all(href=re.compile('elsie'))
print soup.find_all(id=True)  # 把有id的标签都但因出来
print soup.find_all(href=re.compile('elsie'), id='link1')  # 制定拥有多个属性
# 不支持html5 中的data-*属性 但可以用attrs参数定义一个字典
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
print data_soup.find_all(attrs={"data-foo": "value"})
print '-' * 55
# 按CSS搜索 通过class_参数搜索有指定CSS类名的tag
print soup.find_all('a', class_='sister')
# class_ 参数同样接受不同类型的过滤器，字符串 正则 方法 True
print soup.find_all(class_=re.compile('itl'))
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
print soup.find_all(class_=has_six_characters)  # 打印class长度为6的标签列表
# tag的class属性是多值属性，按照css类名搜索tag中的每个CSS类名
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print css_soup.find_all('p', class_='strikeout')  # 只搜索一个值 就能把标签找出来
print css_soup.find_all('p', class_='body')  # 同上
# 搜索class属性时也可以通过CSS值完美匹配
print css_soup.find_all('p', class_='body strikeout')
# 完美匹配class的值时，如果CSS类名的顺序与实际不符，将搜索不到结果
print soup.find_all('a', attrs={'class': 'sister'})

print '-' * 55
# string参数
print soup.find_all(string='Elsie')
print soup.find_all(string=['Tillie', 'Elsie', 'Lacie'])
print soup.find_all(string=re.compile('Dormouse'))
def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return s == s.parent.string
print soup.find_all(string=is_the_only_string_within_a_tag)
print soup.find_all('a', string='Elsie')
# limit参数 限制返回数量
print soup.find_all('a', limit=2)
# recursive参数 只有find_all()&find()支持这个参数
print soup.html.find_all('title')
print soup.html.find_all('title', recursive=False)  # 只想搜索tag的直接子节点

print '-' * 55

# 像调用 find_all()一样调用tag
print soup.find_all('a')
print soup('a')  # 跟上面这个一样的结果 等价
print soup.title.find_all(string=True)
print soup.title(string=True)  # 等价
# find() find(name, attrs, recursive, string, **kwargs)
print soup.find_all('title', limit=1)
print soup.find('title')  # 等价 直接返回结果 find_all()返回列表
print soup.find('nosuchtag')  # 找不到就返回None
print soup.head.title
print soup.find('head').find('title')  # 等价
# find_parents()&find_parent()
a_string = soup.find(string='Lacie')
print a_string
print a_string.find_parents('a')  # 返回列表 存在这个字符串的标签
print a_string.find_parent('a')  # 返回结果 存在这个字符串的标签
print a_string.find_parent('p')  # 返回结果 存在这个字符串的<p>标签
print a_string.find_parents('p', class_='title')  # 返回了一个空
# find_next_siblings() & find_next_sibling()
first_link = soup.a  # 没特别说明就是打印第一个
print first_link
print first_link.find_next_siblings('a')  # 返回列表打印第一个之后的所有
first_story_paragraph = soup.find('p', 'story')
print first_story_paragraph.find_next_sibling('p')  # 返回结果 只打印这个标签内的东西
# find_previous_sibings() & find_previous_sibling()
last_link = soup.find('a', id='link3')
print last_link  # 只返回这个标签
print last_link.find_previous_siblings('a')  # 返回列表 符合条件的前面的兄弟节点
first_story_paragraph = soup.find('p', 'story')
print first_story_paragraph.find_previous_sibling('p')  # 直接返回第一个符合条件的前面的兄弟节点
# 总结：末尾有s的是列表 没有s的直接标签

print '-' * 55

# find_all_next() & find_next()
first_link = soup.a
print first_link
print first_link.find_all_next(string=True)   # 列表 从这个开始所有往下的字符串都显示
print first_link.find_next('p')  # 直接结果 这个之后的<p>都打印
# find_all_previous() & find_previous
first_link = soup.a
print first_link
print first_link.find_all_previous('p')  # 返回列表 返回所有符合条件的节点
print first_link.find_previous('title')  # 返回第一个符合条件的节点

print '-' * 55

# CSS选择器 是一种模式 选择需要添加样式的元素
print soup.select('title')  # 返回列表 <title>标签
print soup.select("p:nth-of-type(3)")
print soup.select('body a')  # 返回列表 <body>里面的<a>标签
print soup.select('html head title')  # 返回列表 这好像是一个详细的路径
print soup.select('head > title')  # head 下的直接子标签 title
print soup.select('p > a')  # p下面的直接子标签a
print soup.select('p > a:nth-of-type(2)')  # p 下面a标签里面的第二个标签
print soup.select('p > #link1')  # p 下面的含有link1的标签
print soup.select('body > a')  # 没有就是个空[]
print soup.select('#link1 ~ .sister')  # 不含有link1 含有sister 的标签
print soup.select('#link1 + .sister')  # 含有link1 含有sister 的标签
# 通过CSS类名来查找
print soup.select('.sister')  # 返回标签 所有含有sister
print soup.select('[class~=sister]')  # 结果同上
# 通过tag的id查找
print soup.select('#link1')  # 返回含有这个的标签
print soup.select('a#link1')  # 同上
# 通过用多种CSS查看器查询元素
print soup.select('#link1, #link2')  # 返回含有这两个的标签
# 通过是否存在某个属性来查找
print soup.select('a[href]')  # 有这个属性的标签全打出来
# 通过属性的值来查找
print soup.select('a[href="http://example.com/elsie"]')
print soup.select('a[href^="http://example.com/"]')
print soup.select('a[href$="tillie"]')
print soup.select('a[href*=".com/el"]')
# 通过语言设置来查找
multilingual_markup = """
<p lang="en">Hello</p>
<p lang="en-us">Howdy, y'all</p>
<p lang="en-gb">Pip-pip, old fruit</p>
<p lang="fr">Bonjour mes amis</p>
"""
multilingual_soup = BeautifulSoup(multilingual_markup, 'lxml')
print multilingual_soup.select('p[lang|=en]')
# 返回查找到的第一个元素
print soup.select_one('.sister')
