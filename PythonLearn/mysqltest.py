#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: mysqltest.py
@time: 2018/1/8 2:54
"""

import pymysql.cursors

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'zhyea.com',
    'db': 'employees',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database
connection = pymysql.connect(**config)