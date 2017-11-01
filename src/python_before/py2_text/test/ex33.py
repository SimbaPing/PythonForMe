# -*- coding:utf-8 -*-
i = 0  # 两个简单的赋值
numbers = []  # 这是一个列表

while i < 6:  # 开始循环 打印到False 才进行下面循环
    print "At the top i is %d" % i  # 打印rang（0， 6）
    numbers.append(i)  # 现在i 添加到number

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
