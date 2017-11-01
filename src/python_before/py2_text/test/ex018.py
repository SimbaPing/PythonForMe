# -*- coding:utf-8 -*-
# 通过argv实现def的功能
from sys import argv

script, arg1, arg2 = argv

print_two = "arg1: %s, arg2: %s" % (arg1, arg2)
print_two_again = print_two
print_one = arg1
print_none = "I got nothin"

print print_two
print print_two_again
print print_one
print print_none
