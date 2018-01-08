#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: client.py
@time: 2018/1/8 21:51
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 1233

s.connect((host, port))

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
