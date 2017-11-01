# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-15 21:10:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-17 00:53:25

import urllib
import urllib2
import urlparse
import re
from bs4 import BeautifulSoup
import pachong


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
