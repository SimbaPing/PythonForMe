# -*- coding:utf-8 -*-


def add(a, b):  # 定义加法
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):  # 定义减法
    print "SUBTTACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):  # 定义乘法
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):  # 定义除法
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit额外加分的难题, type it in anyway.
print "Here is a puzzle."
# 这个要逐个定义，然后逐个打印
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That become: ", what, "Can you do it by hand?"
