# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-02 21:39:21
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-02 21:52:05


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
