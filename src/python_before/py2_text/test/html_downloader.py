# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-16 21:31:45
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-16 21:54:55
import urllib



class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
