import urllib.request
import http.cookiejar
# from bs4 import BeautifulSoup

url = "http://tieba.baidu.com/p/3205263090"
# 创建 cookie 容器
cj = http.cookiejar.CookieJar()
# 代理服务器
proxy_handler = urllib.request.ProxyHandler({'http': '103.87.16.2:80'})
# 创建 opener，里面可以放多个参数，最常见 cookie 和 proxy
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
# 给 urllib.request 安装 opener
urllib.request.install_opener(opener)

values = {'name': 'xxxxxxxx', 'password': 'xxxxxxxx'}
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 '
                  r'Safari/537.36 Core/1.63.4533.400 QQBrowser/10.0.487.400 '
    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}
data = urllib.parse.urlencode(values).encode(encoding='utf8')
req = urllib.request.Request(url, data, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf8')
print(html)
# print(cj)

#
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
