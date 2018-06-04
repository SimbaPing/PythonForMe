#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: weixin_4.py
@Time: 2018/6/4 15:49
"""

# 微信图灵机器人
from wxpy import *

bot = Bot()

my_friend = ensure_one(bot.search('高雪'))
tuling = Tuling(api_key='032f05f0d33e4b649c8be798a3f1cdae')


@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

bot.join()
