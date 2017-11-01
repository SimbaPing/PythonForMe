# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-03 12:09:17
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-03 12:12:01


class Mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASS APPLES!"


thing = Mystuff
thing.apple()
print thing.tangerine
