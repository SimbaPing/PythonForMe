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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 1233

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()

    print("连接地址： %s" % str(addr))

    msg = "欢迎" + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
