#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: server.py
@time: 2018/1/8 21:47
"""

import socket

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机
host = socket.gethostname()

# 端口号
port = 9999

# 绑定端口和主机
serversocket.bind((host, port))

# 设置最大连接数，吵过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址： %s" % str(addr))

    msg = "欢迎" + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
