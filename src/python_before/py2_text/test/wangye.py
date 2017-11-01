# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-17 19:02:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-19 17:51:34
def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print twice.__name__
print twice('word')
print twice(5)

