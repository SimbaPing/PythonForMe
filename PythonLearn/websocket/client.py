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

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 端口号
port = 9999

# 连接服务，主机和端口
s.connect((host, port))

# 接收小于1024的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
