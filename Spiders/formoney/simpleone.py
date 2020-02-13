# -*- coding: utf-8 -*-

# Created with IntelliJ IDEA by Django on 2019/12/2 18:37

import random

# print(random.randint(0, 35) + random.randint(0, 12))

moneyLeft = random.sample(range(1, 35), 5)
moneyRight = random.sample(range(1, 12), 2)
moneyLeft.sort()
moneyRight.sort()

moneyA = random.sample(range(1, 33), 6)
moneyB = random.sample(range(1, 16), 1)
moneyA.sort()
moneyB.sort()

print(moneyLeft, moneyRight)
print(moneyA, moneyB)
