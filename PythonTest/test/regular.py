#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: regular.py
@time: 2017/12/30 20:48
"""

import re

"""
1.基础
1.1 原始字符串 r'expressin'
1.2 匹配单个字符的基本模式，好多...
1.3 编译标志，可以修改正则表达式的某些方面。IGNORECASE 或 I
2. match 和 search
2.1 re.match(pattern, string, flags=0) 与 re.search(pattern, string, flags=0)
    pattern - 这是要匹配的正则表达式。
    string - 这是字符串，它将被搜索用于匹配字符串开头的模式。 |
    flags - 可以使用按位OR(|)指定不同的标志。 这些是修饰符，如下表所列
"""
# 2.2 match 和 search 将 re 模式和可选标志的字符串进行匹配，成功时候返回匹配对象，失败是返回 none
# 2.3 group(num = 0)	此方法返回整个匹配(或特定子组num)
#     groups()	此方法返回一个元组中的所有匹配子组(如果没有，则返回为None)
# 以下两个显示的结果是一样的。

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # 每一个小括号都是一个 group()

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.groups():", matchObj.groups())  # 只返回元组中的值，形式：元组中的字符串
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!!")

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print('searchObj.group()', searchObj.group())
    print('searchObj.groups()', searchObj.groups())
    print('searchObj.group(1)', searchObj.group(1))
    print('searchObj.group(2)', searchObj.group(2))
else:
    print('No search')

print('1' * 20)
# 3. match 检查匹配字符串的开头，search 检查字符串中任意位置的匹配
mObj = re.match(r'dogs', line, re.M | re.I)
if mObj:
    print('match--->mObj.group():', mObj.group())
else:
    print('No match!!')

sObj = re.search(r'dogs', line, re.M | re.I)
if sObj:
    print('search--->sObj.group():', sObj.group())
else:
    print('Nothing found!!')

print('2' * 20)
# 4. 搜索和替换 re 模块中最重要的是 sub
# 4.1 re.sub(pattern, repl, string, max=0)
#     此方法使用repl替换所有出现在RE模式的字符串，替换所有出现，除非提供max。此方法返回修改的字符串。
phone = "2018-959-559 # This is Phone Number"
num = re.sub(r'#.*$', '', phone)
print('Phone num:', num)

num = re.sub(r'\D', '', phone)
print('Phone num:', num)

print('3' * 20)
# 5. 修饰符选项标志，使用异或（|）
# 6. 模式，除了控制字符（+ ? . * ^ $ () [] {} \|），所有字符都与其自身匹配，可以通过反斜杠将其转换为控制字符
# 7. 正则表达式的各种示例...
