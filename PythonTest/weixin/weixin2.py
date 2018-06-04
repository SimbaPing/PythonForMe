#! /usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from echarts import Echart, Legend, Pie
# 微信好友男女比例
itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female = other = 0


for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])

print('男性好友：%.2f%%' % (float(male) / total * 100))
print('女性好友：%.2f%%' % (float(female) / total * 100))
print('其他：%.2f%%' % (float(other) / total * 100))

# 下面可以理解为一个可视化，但是没有做好，我很惭愧

# chart = Echart('%s 的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value': male, 'name': u'男性好友：%.2f%%' % (float(male) / total * 100)},
#                {'value': female, 'name': u'女性好友：%.2f%%' % (float(female) / total * 100)},
#                {'value': other, 'name': u'其他好友：%.2f%%' % (float(other) / total * 100)}],
#               radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# del chart.json["xAxis"]
# del chart.json["yAxis"]
# chart.plot()
