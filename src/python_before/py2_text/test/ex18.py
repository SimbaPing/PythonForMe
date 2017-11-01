# -*- coding:utf-8 -*-

# this one is like your scripts with argv


def print_two(*args):  # 定义了*args参数集合
    arg1, arg2 = args  # 里面有两个
    print "arg1: %r, arg2: %r" % (arg1, arg2)  # 打印这两个


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  # 定义了两个
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument


def print_one(arg1):  # 定义了一个
    print "arg1: %r" % arg1  # 打印一个

# this one takes no arguments


def print_none():  # 定义了一个空的
    print "I got nothin'."  # 打印这个

# 先写的问题后写的答案，这个就是答案


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
