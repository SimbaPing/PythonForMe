# -*- coding:utf-8 -*-
def cheese_and_crackes(cheese_count, boxes_of_crackers):  # 定义了一个参数及其打印
    print "You have %d cheeses!" % cheese_count  # %d只能格式化数字
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"  # 最后有个换行符，好评


print "We can just give the function numbers directly:"
cheese_and_crackes(20, 30)  # 看到这个 直接打印def里面的东西


print "OR, we can use variables from our script:"
amount_of_cheese = 10  # 进行一轮赋值再打印
amount_of_crackers = 50


cheese_and_crackes(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackes(10 + 20, 5 + 6)  # 计算好了再进行打印


print "And we can combine the two, variables and math:"
cheese_and_crackes(amount_of_cheese + 100, amount_of_crackers + 1000)
