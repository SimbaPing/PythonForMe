# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-27 20:04:24
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-27 22:00:49

# 画图，学用circle画圆形。
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=600, height=600, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
