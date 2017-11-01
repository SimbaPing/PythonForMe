# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-28 19:48:39
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-28 19:53:14

# 画椭圆ellipse。　
if __name__ == '__main__':
    from Tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
