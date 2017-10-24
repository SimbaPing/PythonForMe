import re
from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 文档字符串，解析器，字符的编码(被忽略)
# 创建bs对象
soup = BeautifulSoup(html_doc, 'html.parser')
print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print('获取LaCie的链接')
link_Lacie = soup.find('a', href="http://example.com/lacie")
print(link_Lacie.name, link_Lacie['href'], link_Lacie.get_text())

print('正则表达式')
link_re = soup.find('a', href=re.compile(r'ill'))
print(link_re.name, link_re['href'], link_re.get_text())

print('获取p段落文字')
p_note = soup.find('p', class_="title")
print(link_re.name, link_re.get_text())
