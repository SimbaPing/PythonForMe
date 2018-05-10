#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: test180510.py
@Time: 2018/5/10 23:32
"""

import pprint
import pprint as pr
import sys

a = {'lang': 'Python', 'book': 'www.itdiffer.com', 'teacher': 'qiwsir', 'goal': 'from beginner to master'}

pr.pprint(a)

help(pprint.isreadable)

print(pprint.__all__)

print(sys.__doc__)
