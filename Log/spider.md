# python 爬虫日志

---

## 什么是爬虫？

英文名：web crawler 。

URL（Uniform Resource Locator）统一资源定位符。

URL 格式由三部分组成：

- (1)protocol：第一部分就是协议，例如百度使用的就是 https 协议；
- (2)hostname[:port]：第二部分就是主机名(还有端口号为可选参数)，一般网站默认的端口号为 80，例如百度的主机名就是 www.baidu.com，这个就是服务器的地址;
- (3)path：第三部分就是主机资源的具体地址，如目录和文件名等。

---

## 爬虫能做什么？

爬取网页上自己想要的信息。进行分析，存储。

例如：爬取新闻，变成新闻阅读器；故事集；图片；电商价格对比。


---

## 爬虫架构

### 调度器

URL 管理器：管理待爬取的的 URL 和已爬取的 URL

- 防止重复抓取，防止循环抓取
- set() 直接去除重复的元素

网页下载器：将互联网上对应的网页下载到本地的工具

网页解析器：从网页中提取有价值数据的工具

- 正则表达式，模糊匹配，其他三个都是结构化解析
- html.parser
- BeautifulSoup，比较强大，DOM
- lxml

### 实例

目标：

入口页：

URL 格式：后缀需要变化的网页链接

数据格式：标签、属性之类

页面编码：

---

## 审查元素

Elements：
- 选择元素，查看位置
- 模拟器，模拟不同设备显示效果
- 代码区，显示页面代码
- 样式区，显示选中元素所受 CSS 的影响

Network，网络监控功能，俗成抓包：
- 抓什么，通过异步请求获得的数据，如何找到其来源，包括数据，JS，CSS，图片，文档
  - 搜索功能可进行查找
  - 勾选 Preserve log，这样页面刷新或者跳转后，列表不会被清空
  - Filter 栏可以按类型关键字筛选请求
- 怎么抓
  - 请求方法，是 GET 还是 POST
  - 请求附带的参数数据
  - Headers 信息，常用包括 user-agent，host，referer，cookie
  
Sources，查看资源列表和调用 JS。

Console，显示页面的报错和输出，并且可以执行 JS 代码。

## 其他

### 问答

1. 请求方式 GET 和 POST 的区别。
  - GET方式的请求会将请求参数的名和值转换成字符串，并附加在原URL之后，因此可以在地址栏中看到请求参数名和值；且GET请求传送的数据量较小，一般不能大于2kb;
  - POST方式传送的数据量较大，通常认为POST请求参数的大小不受限制，但往往取决于服务器的限制，POST请求传输的数据量总比GET传输的数据量大，而且POST方式发送的请求参数以及对应的值放在HTML HEADER中传输，用户不能在地址栏里看到请求参数值，安全性相对较高。
  - 简单来说，通常使用 POST，如传递参数为普通字符串，少量参数则可用 GET，URL 和参数之间以“？”分隔，多个参数以“&”分隔

## 第三方库有哪些？

urllib:

scrapy:

BeautifulSoup4: from bs4 import BeautifulSoup

requests:

```python


```

html:

### 名词解释

cookie：储存用户本地终端上的数据。

DOM（Document Object Model）文档对象模型。

### 特殊情景处理器

HTTPCookieProcessor<br/>
ProxyHandler<br/>
HTTPSHandler<br/>
HTTPRedirectHandler<br/>
