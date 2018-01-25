#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: html_downloader.py
@time: 2018/1/25 15:39
"""
import urllib.request


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
