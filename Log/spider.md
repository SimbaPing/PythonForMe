# python爬虫日志

---
## 1. 什么是爬虫？
英文名：web crawler 。<br>
URL（Uniform Resource Locator）统一资源定位符。<br>
URL格式由三部分组成：
* (1)protocol：第一部分就是协议，例如百度使用的就是https协议；
* (2)hostname[:port]：第二部分就是主机名(还有端口号为可选参数)，
* 一般网站默认的端口号为80，例如百度的主机名就是www.baidu.com，这个就是服务器的地址;
* (3)path：第三部分就是主机资源的具体地址，如目录和文件名等。

---
## 2. 爬虫能做什么？
爬取网页上自己想要的信息。进行分析，存储。<br>
例如：爬取新闻，变成新闻阅读器；故事集；图片；电商价格对比。<br>
---
## 3. 爬虫架构
### 调度器
URL管理器：管理待爬取的的URL和已爬取的URL
* 防止重复抓取，防止循环抓取
* set()直接去除重复的元素

网页下载器：将互联网上对应的网页下载到本地的工具<br>
网页解析器：从网页中提取有价值数据的工具
* 正则表达式，模糊匹配，其他三个都是结构化解析
* html.parser
* BeautifulSoup，比较强大，DOM
* lxml

### 实例
目标：<br>
入口页：<br>
URL格式：后缀需要变化的网页链接<br>
数据格式：标签、属性之类<br>
页面编码：

---
## 4. 第三方库有哪些？
urllib:<br>
scrapy:<br>
BeautifulSoup4: from bs4 import BeautifulSoup<br>
requests:<br>
html:

---
---
## 名词解释
cookie：储存用户本地终端上的数据。<br>
DOM（Document Object Model）文档对象模型。

---
## 其他
```python
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
     r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
```

---
## 特殊情景处理器
HTTPCookieProcessor<br/>
ProxyHandler<br/>
HTTPSHandler<br/>
HTTPRedirectHandler<br/>

---
## 网页解析器
正则表达式，html.parser，**BeautifulSoup**，lxml