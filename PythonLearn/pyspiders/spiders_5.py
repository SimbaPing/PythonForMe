import urllib
import urllib.request

"""
抓取百度上面搜索Jecvay Notes的网页
"""
data = {'word': 'Jecvay Notes'}
url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url + url_values
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)