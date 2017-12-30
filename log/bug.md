1. 问：TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type s。
答：Request('http://www.douban.com',data  = urllib.parse.urlencode(data).encode(encoding='UTF8'),headers = headers)。 

2. 问：urllib.error.HTTPError: HTTP Error 404: Not Found。
答：添加 cookie 信息。

3. encode 和 decode 区别：
* str->bytes: encode 编码，编码就是将字符串转换成字节码，涉及到字符串的内部表示。
* bytes->str: decode 解码，解码就是将字节码转换为字符串，将比特位显示成字符
* data 里面用 encode(encoding='utf-8')，read() 用 .decode('utf-8')。