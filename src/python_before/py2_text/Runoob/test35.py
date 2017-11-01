# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-24 17:03:31
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-24 17:13:44

# 文本颜色设置。

# 警告
# 这是在Linux系统下的命令行颜色设置
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print Bcolors.WARNING + "警告的颜色字体？" + Bcolors.ENDC
