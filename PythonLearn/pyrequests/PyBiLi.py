# coding=utf-8
import requests
import re


aid = input('请输入av号：')
# 获取bilibili视频地址
url = 'https://www.bilibili.com/video/av' + aid
headers = {'Host': 'www.bilibili.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           'Connection': 'keep-alive'
           }

res = requests.get(url=url, headers=headers).text

vid = re.compile(r'"url":"http(.+?)","backup_url":.+?')
tittle = re.findall(r'<h1 title="(.+?)".*?>', res)[0]
vid_url = 'https' + re.findall(vid, res)[0]
print(tittle, '\n', vid_url)
vid_headers = {
    'Origin': 'https://www.bilibili.com',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
video = requests.get(url=vid_url, headers=vid_headers).content

with open('./video/' + tittle + '.mp4', 'wb+') as f:
    f.write(video)

