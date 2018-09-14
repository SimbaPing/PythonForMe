#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random

print("Hello world!")

print(list(range(2, 11)))

nums = [1, 2, 3, 4, 5]
targets = 123
a = 120
print(len(nums))


# for i in list(range(len(nums) - 1)):
#     for j in list(range(i+1, len(nums))):
#         if nums[i] + nums[j] == target:
#             return [i, j]

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == targets:
            print([i, j])

print(random.randint(1, 2))

print(str(a))
print(list(str(a)))
b = list(str(a))
c = [b[2], b[1], b[0]]
d = list(map(int, c))
e = d[0] * 100 + d[1] * 10 + d[2] * 1
print(e)

m = list(str(a))
n = []
for i in range(0, len(m)):
    n.append(m[len(m) - i - 1])
print(n)
p = list(map(int, n))
q = p[0] * 100 + p[1] * 10 + p[2] * 1
print(q)

print("Hello world!")