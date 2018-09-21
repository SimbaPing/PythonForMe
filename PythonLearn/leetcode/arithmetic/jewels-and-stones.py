#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 9/21/2018 20:24
Filename: jewels-and-stones.py
Contact: uppjs@qq.com
Description: 
"""

J = "aA"
S = "aAAbbb"

list_J = list(J)
list_S = list(S)
end = []
for j in list_J:
    for s in list_S:
        if j == s:
            end.append(s)

print(len(end))
