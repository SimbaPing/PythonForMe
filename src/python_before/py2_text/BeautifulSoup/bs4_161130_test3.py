# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-11-30 22:21:07
# @Last Modified by:   Administrator
# @Last Modified time: 2016-12-02 23:01:50

from bs4 import BeautifulSoup

# 所有的Python对象分为四种：Tag NavigableString BeautifulSoup Comment

# Tag 最重要的属性：name, attributes
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "lxml")
tag = soup.b

# Name
print tag  # <b class="boldest">Extremely bold</b>
print type(tag)  # <class 'bs4.element.Tag'>
print tag.name  # b
    # tag.name = "blockquote"  # 改变名字
    # print tag  # 改变所有的HTML文档

# Attributes
print tag['class']  # 返回列表 ['boldest']
print tag.attrs  # 返回字典 {'class': ['boldest']}
    # tag的属性可以被添加,删除或修改, tag的属性操作方法与字典一样
    # 多值属性：rel, rev, accept-charset, headers, accesskey

id_soup = BeautifulSoup('<p id="my id"></p>', "lxml")
print id_soup.p['id']  # 如果某个属性看起来有多个值，那么这个属性返回字符串

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', "lxml")
print rel_soup.a['rel']  # 单个值返回列表
rel_soup.a['rel'] = ['index', 'contents']  # 添加值
print rel_soup.p  # 打印整个标签 之被添加了进去

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print xml_soup.p['class']  # xml格式 没有多值属性 返回字符串

# NavigableString类 包装tag中的字符串 可以遍历的字符串
print tag.string  # 打印tag的文本内容
print type(tag.string)
unicode_string = unicode(tag.string)  # unicode（）方法
print unicode_string  # 通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串
print type(unicode_string)  # <type 'unicode'>
tag.string.replace_with("No longer bold")  # tag中不能编辑 但可以用relpace_with()方法替换
print tag

# BeautifulSoup 对象表示的是一个文档的全部内容，大部分时候，可以把它当做Tag对象
# 没有 name, attribute. 只包含一个值为[document]的特殊属性 .name
print soup.name  # [document]

# comment 什么玩意
markup = "<b><!--Hey, buddy. Want to by a used parser?--></b>"
soup = BeautifulSoup(markup, "lxml")
comment = soup.b.string
print comment  # 这个是打印字符串 已经好几遍了 擦擦擦
print type(comment)
print soup.b.prettify()  # 漂亮方法

# Beautiful Soup中定义的其它类型都可能会出现在XML的文档中: CData , ProcessingInstruction , Declaration , Doctype .与 Comment，
# 这些类都是 NavigableString 的子类,只是添加了一些额外的方法的字符串独享.
# 用里面的CData来代替注释
from bs4 import CData
cdata = CData('A CDATA block')
comment.replace_with(cdata)
print soup.b.prettify()
