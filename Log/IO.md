# 这是 Python3

---
## 文件 IO

---
* 文件内建函数(open()和file())

``` python
file_name = open(file_name, access_mode = 'r', buffering = -1)
'''
file_name 是要打开文件名的字符串，可包含路径。
access_mode 可选变量，字符串，代表文件打开模式。
* 'r' 或 'U' 模式打开的文件必须是已存在的，读。
* 'w' 模式打开的文件若存在则首先清空，写。
* 'a' 模式追加数据，追加到末尾，追加。
* 其他还有 r+, rb, rb+ 等。
buffering 缓冲方式。
* 0 不缓冲，1 只缓冲一行数据。
* 大于 1 给定缓冲区大小， 不提供或负值使用系统默认缓冲机制。
'''
``` 
*中文写入要加上 encoding="utf-8"。
