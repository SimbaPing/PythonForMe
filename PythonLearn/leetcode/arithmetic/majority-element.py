# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/11/5 23:40
Filename: majority-element.py
Contact: uppjs@qq.com
Description: 
"""

# set 是一个无序且不重复的元素集合。
# 众数：一组数中占比例最多的那个数。


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = set(nums)
    n = len(nums) / 2
    for item in res:
        if nums.count(item) > n:
            print(item)


majorityElement('111222222222333')
