#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: MeizituSpider.py
@time: 2017/12/30 23:51
"""
import scrapy
from scrapy.http import Request, HtmlResponse
import os


class MeizituSpider(scrapy.spiders.Spider):
    name = 'meizitu'  # 爬虫名
    allowed_domians = ['meizitu.com']  # 允许域名列表
    start_urls = ['http://www.meizitu.com/a/']  # 起始链接列表
    for i in range(2, 91):
        start_urls.append('http://www.meizitu.com/a/list_1' + str(i) + '.html')
    #请求头
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'www.meizitu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36'
    }


    def make_requests_from_url(self, url):
        return Request(url, headers=self.headers, dont_filter=True)


