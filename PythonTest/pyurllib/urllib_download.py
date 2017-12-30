import urllib.request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种')
response_1 = urllib.request.urlopen(url)
print(response_1.getcode())
print(len(response_1.read()))

print('第二种')
request = urllib.request.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response_2 = urllib.request.urlopen(request)
print(response_2.getcode())
print(len(response_2.read()))

print('第三种')
cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener=opener)
response_3 = urllib.request.urlopen(url)
print(response_3.getcode())
print(cookie)
print(len(response_3.read()))
