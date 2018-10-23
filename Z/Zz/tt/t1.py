# -*- coding:utf-8 -*-

"""
Created with IntelliJ IDEA
Created by uppjs on 2018/10/10 9:10
Filename: t1.py
Contact: uppjs@qq.com
Description: 
"""

l1 = [1, 2, 3, 1, 3]

for i in l1:
    s1 = int(''.join(str(i)))
print(s1)
# l1.remove(1)
# print(l1)

print('****************************************')
l2 = '1234'
l20 = []
for i in l2:
    l20.append(int(i))

print(list(l2))

print(l20)

l21 = ''.join(list(l2))


# 数字型字符串可变为：
# 1. int(str) - 变为数字
# 2. list(str) - 变为字符串列表
# 3. int(i) for i in list(str) - 变为数字列表
# TODO: [1, 2, 3, 4] ==> 1234
lc = [1, 2, 3, 4]
ld = []
for i in lc:
    ld.append(str(i))
print(ld)
le = ''.join(ld)
print(int(le))
print(type(int(le)))
print(1 + int(le))
print('****************************************************')

d = []
for i in lc:
    d.append(str(i))
e = ''.join(d)
f = 1 + int(e)
g = []
print(str(f))
for i in str(f):
    g.append(int(i))
print(g)

print("uppjs")
