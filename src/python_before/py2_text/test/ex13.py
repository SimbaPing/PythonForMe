# -*- coding:utf-8 -*-

from sys import argv # import 语句 argv（argument variable）参数变量就是解包（unpack） 

script, first, second, third = argv # 把 argv 中的东西解包，将所有参数一次赋予左边的变量名

print "The script is called:", script # 打印脚本名
print "Your first variable is:", first # 打印第一个字符，下同
print "Your second variable is:", second
print "Your third variable is:", third

# import 称为功能，模组    你需要把 sys 模组 import 进来
#也有人叫库(libraries), 不过现在还是叫模组