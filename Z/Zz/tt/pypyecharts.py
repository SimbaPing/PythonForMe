#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: pypyecharts
.......date: 2018/8/28 23:26
created with IntelliJ IDEA
description:
"""

from pyecharts import Map
districts = ['运河区', '新华区', '泊头市', '任丘市', '黄骅市', '河间市', '沧县', '青县', '东光县', '海兴县', '盐山县', '肃宁县', '南皮县', '吴桥县', '献县', '孟村回族自治县']
areas = [109.92, 109.47, 1006.5, 1023.0, 1544.7, 1333.0, 1104.0, 968.0, 730.0, 915.1, 796.0, 525.0, 794.0, 600.0, 1191.0, 387.0]
map_1 = Map("沧州市图例－各区面积", width=1200, height=600)
map_1.add("", districts, areas, maptype='沧州', is_visualmap=True, visual_range=[min(areas), max(areas)],
          visual_text_color='#000', is_map_symbol_show=False, is_label_show=True)
map_1.render()
