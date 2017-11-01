# -*- coding:utf-8 -*-

from sys import argv

script, user_name = argv  # 源码名 文件名 参数变量
prompt = '>'  # 提示符 > 一个简单的赋值

print "Hi %s, I'm the %s script." % (user_name, script)  # 打印 格式化数据
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)  # 打印提示 > 内容又赋值给 likes

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)  # 三引号格式化数据 在最后 %（）
