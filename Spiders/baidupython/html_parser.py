#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: html_parser.py
@time: 2018/1/25 15:40
"""
import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):  # 解析出新的 url 列表，和数据
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)  # 本地方法，获取新的 url
        new_data = self._get_new_data(page_url, soup)  # 本地方法，获取页面中的数据
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup, summary_node=None):
        if summary_node is None:
            return 
        
        res_data = {'url': page_url}

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
