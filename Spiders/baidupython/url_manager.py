#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: url_manager.py
@time: 2018/1/25 15:40
"""


class UrlManager(object):
    def __init__(self):  # 初始化
        self.new_urls = set()  # 待爬取 url 列表
        self.old_urls = set()  # 已爬取 url 列表

    def add_new_url(self, url):
        if url is None:  # 如果 url 不存在，那就不添加
            return
        if url not in self.new_urls and url not in self.old_urls:  # 如果 url 不在新旧里面
            self.new_urls.add(url)  # 那么就把他添加进待爬取 url

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:  # 如果 urls 不存在或者长度等于0，那么不添加
            return
        for url in urls:  # 将 url 挨个添加进 urls
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 从 new_urls 里拿出一个来并从里面删除
        self.old_urls.add(new_url)  # 将拿出的这个添加进已爬取 url
        return new_url  # 返回这个拿出的 url


