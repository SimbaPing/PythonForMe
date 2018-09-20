#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 9/21/2018 06:00
Filename: palindrome-number.py
Contact: uppjs@qq.com
Description: 
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x >= 0:
        # 因为知道是一个整数，所以将它变为字符串
        str_x = str(x)
        # 将字符串倒置
        str_x = str_x[::-1]
        # 将字符串还原为整数
        y = int(str_x)
        if x == y:
            print(True)
        else:
            print(False)
    else:
        print(False)


if __name__ == '__main__':
    p = int(input("请输入整数："))
    isPalindrome(p)
