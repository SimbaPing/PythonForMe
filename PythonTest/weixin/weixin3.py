#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: weixin3.py
@Time: 2018/6/4 15:12
"""

from wxpy import *

bot = Bot()

# 找到好友 （名称，性别，城市）
my_friend = bot.friends().search('高雪', sex=FEMALE, city='莱芜')[0]
print(my_friend)
# 发送给这个好友消息
my_friend.send('Hello WeChat!')
# 发送图片
my_friend.send_image('mypic.jpg')
