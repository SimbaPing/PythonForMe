# 强行头部

1. 问：TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type s。
答：Request('http://www.douban.com',data  = urllib.parse.urlencode(data).encode(encoding='UTF8'),headers = headers)。 

2. 问：urllib.error.HTTPError: HTTP Error 404: Not Found。
答：添加 cookie 信息。

3. encode 和 decode 区别：
* str->bytes: encode 编码，编码就是将字符串转换成字节码，涉及到字符串的内部表示。
* bytes->str: decode 解码，解码就是将字节码转换为字符串，将比特位显示成字符
* data 里面用 encode(encoding='utf-8')，read() 用 .decode('utf-8')。

4. 将图片下载到本地文件夹，并且按照顺序编号。
```python
import urllib.request

imgList = []  # 这是一个列表
imgName = 0  # 列表的起始数字
for imgPath in imgList:  # 将列表逐行打印变成 imgPath
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    f = open(str(imgName) + ".jpg", 'wb')  # 新建图片文件
    f.write((urllib.request.urlopen(imgPath)).read())  # 然后读取网页中的图片文件读取然后写入之前建好的文件中
    f.close()  # 做完记得关闭
    imgName += 1
```

5. 爬虫
单个网页内容：模拟浏览器登陆网站→用正则表达式在标签中获取自己想要的信息→将信息下载至本地。

临时：目前的难点是正则表达式，网页之间的游走，如何有组织的写类和函数

6. requests 爬取后中文乱码。
r = requests.get(url)
**r.ending = 'gbk'**，中文编码 gbk

7.