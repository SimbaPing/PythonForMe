#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created with IntelliJ IDEA
@Author: Ping
@Contact: fpsping@163.com
@File: testclass.py
@Time: 2018/5/15 23:18
"""

print("第一个：")


class MyClass:
    # 一个简单的类实例
    i = 12345

    @staticmethod
    def f():
        return 'hello world'


x = MyClass()

print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

print("第二个：")


class Test:

    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

print("第三个：")


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

print("第四个：")


class People:
    name = ""
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" %(self.name, self.age))


p = People('uppjs', 10, 30)
p.speak()


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说：我 %d 岁了， 我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student('Ken', 10, 60, 3)
s.speak()
