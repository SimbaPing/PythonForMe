#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/9/21 21:48
Filename: skyline.py
Contact: uppjs@qq.com
Description:
"""
# TODO 保持城市天际线，这个是中等难度，瞟了一眼答案，决定先等等
# TODO 自己也构思了一下，但是觉得太复杂

grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]

grid_1 = grid[0]
grid_2 = grid[1]
grid_3 = grid[2]
grid_4 = grid[3]
grid_a = [grid_1[0], grid_2[0], grid_3[0], grid_4[0]]

print(grid[0][0])

# 求列表中的最大值
g = grid_3

g_max = g[0]
g_min = g[0]
for i in g:
    if i > g_max:
        g_max = i
    if i < g_min:
        g_min = i

print(g_max, g_min)


