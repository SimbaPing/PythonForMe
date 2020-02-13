# -*- coding: utf-8 -*-

# Created with IntelliJ IDEA by Django on 2019/6/15 22:58
# 猜数字，运用了 random


import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break

print('你总共踩了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
