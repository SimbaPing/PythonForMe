# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-21 19:35:47
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-21 21:05:42
# 输入指定日期格式
import datetime

if __name__ == '__main__':

    print datetime.date.today().strftime('%d/%m/%Y')
    BD = datetime.date(1942, 1, 5)
    print BD.strftime('%d/%m/%Y')
    BD = BD + datetime.timedelta(days = 1)
    print BD.strftime('%d/%m/%Y')
    BD = BD.replace(year = BD.year + 1)
    print BD.strftime('%d/%m/%Y')
