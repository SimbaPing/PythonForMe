# -*- coding: UTF-8 -*-

import urllib.request

'''
# 里面有错误但是不懂到底哪里有问题。
'''

# 发送数据 和 header

# 网页
url_first = 'http://www.python.org/'
url = 'http://localhost/login.php'

# 制造虚假浏览器和表单
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'act': 'login', 'login[email]': 'abc@abc.com', 'login[password]': '123456'}
headers = {'User-Agent': user_agent}  # 让目标网页以为我是从这进去的
data = urllib.parse.urlencode(values)  # 将登陆信息写入 data
data = data.encode('ascii')

# 将他们解析出来
req = urllib.request.Request(url, data, headers)  # 将原链接与表头、表单进行结合
response = urllib.request.urlopen(req)  # 打开做好的网页
html = response.read()  # 读取网页数据
print(html)  # 打印网页
