#python爬虫日志

---
##1. 什么是爬虫？
英文名：web crawler 。
URL（Uniform Resource Locator）统一资源定位符。
URL格式由三部分组成：
* (1)protocol：第一部分就是协议，例如百度使用的就是https协议；
* (2)hostname[:port]：第二部分就是主机名(还有端口号为可选参数)，
* 一般网站默认的端口号为80，例如百度的主机名就是www.baidu.com，这个就是服务器的地址;
* (3)path：第三部分就是主机资源的具体地址，如目录和文件名等。

---
##2. 爬虫能做什么？
爬取网页上自己想要的信息。进行分析，存储。
例如：爬取新闻，变成新闻阅读器；故事集；图片；电商价格对比。
###爬虫步骤：
调度器：
URL管理器：管理待爬取的的URL和已爬取的URL
* 防止重复抓取，防止循环抓取
* set()直接去除重复的元素
网页下载器：将互联网上对应的网页下载到本地的工具
网页解析器：从网页中提取有价值数据的工具
* 正则表达式，模糊匹配，其他三个都是结构化解析
* html.parser
* BeautifulSoup，比较强大，DOM
* lxml
###实例
目标：
入口页：
URL格式：后缀需要变化的网页链接
数据格式：标签、属性之类
页面编码：

---
##3. 第三方库有哪些？
urllib:
scrapy:
BeautifulSoup4:

---
##4. urllib
详见：PythonForMe\src\python_test\pyurllib
###4.1 urllib步骤
url:网址。 
values：{登陆表单}（字典）

headers：{'User-Agent':user_agant, 
* 'Regerer':r'网址'
* 'connection':'连接状态'}模拟浏览器（字典）
data：urllib.parse.urlencode(values) 将表单数据变为 data，Post 提交的数据

req：urllib.request.Request(url, data, headers) 用这三个东西请求
response：urllib.request.urlopen(req) 正式打开网页 并响应
html: response.read()读取这个响应
print(html) 答应这个网页，或者做其他操作
###4.2 urllib其他
urllib.request.Request(url, data=None, headers={}, method=None)
使用Request（）来包装请求，再通过urlopen（）获取页面。
* 
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码

urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None)
urlencode（）主要作用就是将url附上要提交的数据。

urllib.request.ProxyHandler(proxies=None)
当需要抓取的网站设置了访问限制，这时就需要用到代理来抓取数据。

urllib.request.ProxyHandler(proxies=None)
当需要抓取的网站设置了访问限制，这时就需要用到代理来抓取数据。

---
##5. BeautifulSoup
html网页——创建beautsoup对象——搜索节点（find_all、find）——访问节点（名词、属性、文字）

---
##名词解释
cookie：储存用户本地终端上的数据。
DOM（Document Object Model）文档对象模型

---
##其他
headers = {
* 'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
* r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
* 'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
* 'Connection': 'keep-alive'
}