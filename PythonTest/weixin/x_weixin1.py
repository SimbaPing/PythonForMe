from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()


def get_new1():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


def send_news():
    try:
        my_friend = bot.friends().search(u'徒手敬岁月')[0]
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"来自爸爸的心灵鸡汤！")
        t = Timer(86400, send_news)
        t.start()
    except:
        my_friend = bot.friends().search('常念')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    send_news()
