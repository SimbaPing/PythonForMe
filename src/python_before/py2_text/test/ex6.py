# -*- coding:utf-8 -*-

x = "There are %d type of people." % 10 # 后面的赋值给x 格式化字符
binary = "binary" # 赋值
do_not = "don't" # 赋值
y = "Those who know %s and those who %s." % (binary, do_not) # 后面的赋值给y 格式化字符

print x # 打印x
print y # 打印y

print "I said: %r." % x # 打印有格式化字符的string
print "I also said: '%s'." % y # 打印有格式化字符的string

hilarious = False # ？
joke_evaluation = "Isn't that joke so funny?! %r" # 赋值 格式化字符 ？

print joke_evaluation % hilarious # 打印

w = "This is the left side of..." # 赋值
e = "a string with a right side." # 赋值

print w + e # 打印并运算
