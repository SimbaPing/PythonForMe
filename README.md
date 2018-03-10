# PYTHON 3

## 1. Python 基础
**编码**：Python 3 源码文件以 UTF-8 编码，所有字符串都是 Unicode 字符串。
可通过 `# -*- coding: cp-1252 -*- `来指定。

**标识符**：
* 第一个字符必须是字母表中字母或下划线'_'。
* 标识符的其他的部分有字母、数字和下划线组成。
* 标识符对大小写敏感。

**Python 保留字**。

**注释**：单行 `# 这里面是注释`，多行注释`'''这里是多行'''` `"""这里是多行"""`。

**行与缩进**：用缩进来表示代码块。缩进不一致会导致错误。

**多行语句**：末尾加反斜杠`\`来实现。大中小括号中不需要加。

**数据类型**：整数、长整数、浮点数、复数。

**字符串**：
* 单引号和双引号的使用完全相同。
* 使用三引号可以指定一个多行字符串。
* 转义符`\`。
* 自然字符串，通过在字符串前加 r 或 R。
* 允许处理 Unicode 字符串，在前面加 u 或 U。
* 字符串是不可变的。

**空行**：空行也是代码的一部分

**等待用户输入**：input("用户输入")。

**同一行显示多条语句**：末尾使用`;`结尾。

**多个语句构成代码组**：
* 缩进相同的一组语句构成一个代码块，我们称之代码组。
* 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
* 我们将首行及后面的代码组称为一个子句(clause)。

**print 输出**：是默认换行的，如果想实现不换行加`end=""`，这样`print(x, end="")`。

**导入模块**：import 和 from...import.

**命令行参数**：python -h。

**解释器**：交互式编程，脚本式编程。

**标准库概览**：os, glob, sys, re, math, random, urllib, datetime, zlib, timeit, doctes, unittest

---
## 2. 基本数据类型
在 Python 中，变量就是变量，我们所说的“类型”是变量所指的内存中对象的类型。<br/>
等号左边是变量名，右边是存储在变量中的值。<br/>
Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。<br/>
六种数据类型：Numbers（数字），String（字符串），List（列表），Tuple（元组），Sets（集合），Dictionaries（字典）<br/>

### Numbers
int，float，bool，complex。<br/>
数值的除法`/`总会返回一个浮点数，使用`//`会获得整数。<br/>
在混合计算时，Python 会把整型转换为浮点数。<br/>

### String
字符串用`' ' " "`，意思是一样的。<br/>
转义字符`\`，如果不想字符串转义，例如文件夹，在字符串前面加`r`。<br/>
三引号来表示多行字符串。<br/>
串联字符串 `+`，重复字符串 `*`。<br/>
字符串索引：从左往右，从0开始一次增加；从右往左，从-1开始依次减少。<br/>
一个字符就是长度为1的字符串。<br/>
字符串不能改变。<br/>

### List
Python 中使用最频繁的数据类型。<br/>
和字符串一样，列表也能被索引和切片。<br/>
列表中的元素是可以改变的。<br/>

### Tuple
元组元素不能修改。<br/>
也可以被索引和切片。<br/>

### Sets
是一个无序不重复元素的集。<br/>
基本功能是进行成员关系测试和消除重复元素。<br/>

### Dictionaries
是一种映射类型（mapping type），是一个无序的 `键:值` 集合。<br/>
字典的关键字必须为不可变类型，且不能重复。<br/>

## 3. 运算符
### 算术运算符
### 比较（关系）运算符
### 赋值运算符
### 逻辑运算符
### 位运算符
### 成员运算符
### 身份运算符
### 运算符优先级

---
## 4. 控制语句

### 条件控制
if<br/>
if...else...<br/>

### 循环语句
while<br/>
while...else...<br/>
for<br/>
break 和 continue<br/>
pass<br/>

### 迭代器
iter()<br/>
next()<br/>

### 生成器（generator）
yield<br/>

---
## 5. 函数
定义一个函数<br/>
函数调用<br/>
参数传递<br/>
参数<br/>
匿名函数<br/>
return 语句<br/>
变量作用域<br/>

---
## 6. 输入和输出

---
## 7. File

---
## 8. 错误和异常

语法错误<br/>
异常<br/>
异常处理<br/>
抛出异常<br/>
用户自定义异常<br/>
定义清理行为<br/>
预定义的清理行为<br/>

---
## 9. 正则表达式
匹配成功返回一个匹配的对象，否则返回 None。<br/>
re.match(pattern, strings, flags=0)，<br/>
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
* pattern 正则表达式
* strings 要匹配的字符串
* flags 用于控制正则表达式的匹配方式，例如区分大小写、多行匹配等

re.search(pattern, strings, flags=0)，<br/>
扫描整个字符串并返回第一个成功的匹配。<br/>

re.sub(pattern, repl, string, max=0)<br/>

\d digit数字，\s space空格，\w word单词。

re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）。<br/>
M(MULTILINE): 多行模式，改变'^'和'$'的行为。<br/>
S(DOTALL): 点任意匹配模式，改变'.'的行为。<br/>
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定。<br/>
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性。<br/>
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。<br/>

---
## 10. 面向对象
类定义<br/>
类对象<br/>
类的方法<br/>
继承<br/>
多继承<br/>
方法重写<br/>
类属性和方法<br/>

---
## 11. CGI 编程
CGI（Common Gateway Interface），通用网关接口。<br/>

---
## 12. MySQL 数据库连接
安装<br/>
数据库连接<br/>
创建数据库表<br/>
数据库插入操作<br/>
数据库查询操作<br/>
数据可更新操作<br/>
删除操作<br/>
执行事务<br/>
错误处理<br/>

---
## 13. 网络编程
Socket 套接字，应用程序通过“套接字”向网络发出请求或者应答网络请求，使主机间或计算机上的进程间可以通讯。<br/>
Python 提供了两个级别访问的网络服务：
* 低级别 Socket，可以访问底层操作系统 Socket 的全部方法。
* 高级别 SocketServer，提供了服务器中心类，可以简化网络服务器的开发。

socket.socket([family[, type[, proto]]])
* family：套接字家族可以使用 AF_UNIX 或 AF_INET。
* type：套接字类型可以根据是面向连接的还是非连接分为 SOCK_STEAM 或 SOCK_DGRAM。
* protocol：一般默认值是0。

Socket 对象內建方法。
* 服务端套接字
* 客户端套接字
* 公共用途的套接字函数

---
## 14. JSON
JSON（JavaScript Object Notation） 是一种轻量级的数据交换格式。基于 ECMAScript 的一个子集。<br/>
Python3 中可以使用 json 对 JSON 数据进行解码，包含两个函数：
* json.dumps() 对数据进行编码
* json.loads() 对数据进行解码

---
## 15. CGI 编程
CGI 目前由 NCSA 维护。<br/>
CGI（Common Gateway Interface），通用网关接口，他是一段程序，运行在服务器上。<br/>
网页浏览<br/>
CGI 框架<br/>
Web 服务器支持与配置<br/>
HTTP 头部<br/>
CGI 环境变量<br/>
GET 和 POST 方法<br/>
CGI 中使用 Cookie<br/>
文件下载对话框<br/>

---
## 16. 日期和时间

---
## 17. 多线程
Python3 使用线程有两种方式：函数或者用类来包装线程对象。<br/>
线程模块<br/>
使用 threading 模块来创建线程<br/>
线程同步<br/>
线程优先级队列<br/>

======
以上
<meta http-equiv="refresh" content="2">

