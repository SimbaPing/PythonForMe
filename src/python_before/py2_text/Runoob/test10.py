# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 22:19:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-31 22:26:07

# 暂停一秒输出
import time
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
