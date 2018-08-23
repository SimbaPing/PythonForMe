#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: py-numpy
.......date: 2018/8/23 23:28
created with IntelliJ IDEA
description:
"""

import numpy as np

a0 = np.array([[1, 2], [3, 4], [5, 6]])
print(a0)
a = np.zeros(6)
print(a)
a = np.zeros((2, 3))
print(a)
a = np.ones((2, 3))
print(a)
a = np.empty((2, 3))
print(a)
a = np.arange(6)
print(a)
a = np.arange(1, 9, 2)
print(a)
a = np.linspace(0, 10, 7)
print(a)
a = np.logspace(0, 4, 5)
print(a)

b0 = np.array([[10, 20], [30, 40], [50, 60]])
print(np.vstack((a0, b0)))
print(np.hstack((a0, b0)))
