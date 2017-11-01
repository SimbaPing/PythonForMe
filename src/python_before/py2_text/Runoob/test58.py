# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 22:08:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 22:17:46

# 画图，学用rectangle画方形。
if __name__ == '__main__':
    from Tkinter import *
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0 = 200
    y0 = 200
    y1 = 262
    x1 = 262
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()

