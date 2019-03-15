#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
.....author: Ping
....contact: uppjs@qq.com
.......file: class-2
.......date: 2018/7/27 22:51
created with IntelliJ IDEA
description: 继承
"""


class Animal(object):

    @staticmethod
    def run():
        print('Animal is running.')


class Dog(Animal):

    def run(self):
        print('Dog is running.')

    @staticmethod
    def eat():
        print('Eating meat.')


class Cat(Animal):

    def run(self):
        print('Cat is running.')


class Tortoise(Animal):

    def run(self):
        print('Tortoise is running slowly.')


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Tortoise())
