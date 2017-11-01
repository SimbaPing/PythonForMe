# -*- coding:utf-8 -*-

formatter = "%r %r %r %r" # 格式化程序 

print formatter % (1, 2, 3, 4) # 打印 formatter ，值在括号里
print formatter % ("one", "two", "three","four") #  同上
print formatter % (True, False, False, True) # 同上
print formatter % (formatter, formatter, formatter, formatter) # 同上
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I　said goodnight."
	) # 打印这些话，但是是在同一行中