#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/26 20:52
Filename: longest-common-prefix.py
Contact: uppjs@qq.com
Description: 
"""

sss = ["flooooooower", "flooooooooow", "flooooooooooight"]


def longestCommonPrefix(aaa):
    if len(aaa) == 0:  # 1. 如果字符串长度为0，那么返回  空
        return ""
    ss = aaa[0]  # 2. 列表中第一个字符串
    Min = len(ss)  # 3. 列表的长度
    for i in range(1, len(aaa)):  # 4. 对除第0个字符串之外的进行 for，以数字形式
        j = 0  # 5. 设置个0？
        p = aaa[i]  # 6. 开始进行第一个字符串操作
        # ↓ 7. 如果第0个字符串的长度不为0 and 其他字符串依次不为0 and 第0个字符串中的第0个字母和其他中的第0个相等，就发生下面的事
        while j < Min and j < len(p) and p[j] == ss[j]:
            j += 1
        # Min = 100 if Min < j else j
        if Min < j:
            Min = Min
        else:
            Min = j
    print(ss[:Min])


longestCommonPrefix(sss)


a, b = 1, 2
c = [a, b][a > b]
print(c)

a1 = True
b1 = 1
c1 = 2
print(a1 and b1 or c1)
