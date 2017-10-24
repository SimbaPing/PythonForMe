import urllib.request

# 最简单的方法

url = 'https://www.baidu.com/'
response = urllib.request.urlopen(url)
html = response.read()
print(html)

