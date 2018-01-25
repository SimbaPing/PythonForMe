#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: spider_main.py
@time: 2018/1/25 15:39
"""
from Spiders.baidupython import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):  # 初始化
        self.urls = url_manager.UrlManager()  # 将 url 管理器实例化为 urls
        self.downloader = html_downloader.HtmlDownloader()  # 将 html 下载器实例化为 Downloader
        self.parser = html_parser.HtmlParser()  # 将 html 解析器实例化为 parser
        self.outputer = html_outputer.HtmlOutputer()  # 将 html 输出器 实例化为 outputer

    def craw(self, root_url):  # 主要函数
        count = 1  # 给抓取链接添加数字列表
        self.urls.add_new_url(root_url)  # 将初始链接添加进 urls 链接池
        while self.urls.has_new_url():  # 如果链接池中有新链接
            new_url = self.urls.get_new_url()  # 获取这个链接添加进 下载器
            print('craw%d:%s', count, new_url)
            html_cont = self.downloader.download(new_url)  # 在下载器中将这个链接下载下来
            new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析出新的链接和网页中的数据
            self.urls.add_new_urls(new_urls)  # 将链接添加进新的链接池
            self.outputer.collect_data(new_data)  # 将数据收集到 outputer

            if count == 100:
                break


            count += 1

        self.outputer.output_html()  # ？？输出收集好的数据


if __name__ == '__main__':  # 入口
    root_url = 'https://baike.baidu.com/item/Python/407313'  # 入口 url
    obj_spider = SpiderMain()  # 将类实例化
    obj_spider.craw(root_url)  # 调用这个类中的函数，也就是主要抓取函数
