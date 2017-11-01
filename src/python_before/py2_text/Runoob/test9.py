# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-20 22:11:19
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-20 22:18:25

# 暂停一秒打印
import time
myD = {1:'a', 2:'b'}
for key, value in dict.items(myD):  # item 方法
    print key, value
    time.sleep(2)
