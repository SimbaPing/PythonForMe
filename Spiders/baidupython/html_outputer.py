#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@author: Ping
@contact: fpsping@163.com
@file: html_outputer.py
@time: 2018/1/25 15:40
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):  # 收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  # 将收集好的数据放到一个 html 页面中
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<meta charset=\'utf-8\'>")
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
