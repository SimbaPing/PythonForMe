# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-05 19:19:14
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-05 20:43:14


from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
    return wrappedFunc


@tsfunc
def foo():
    pass


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
