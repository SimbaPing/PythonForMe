import urllib.request

# 采用 Request

url = 'https://www.baidu.com/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
print(html)