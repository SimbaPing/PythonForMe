# -*- coding:utf-8 -*-
people = 30
cars = 40
buses = 15

if cars > people:  # 如果
    print "We should take the cars."
elif cars < people:  # 再如果
    print "We should not take the cars."
else:  # 不然
    print "We can't decide."

if buses > cars:
    print "This too many cars."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alight, let's just take the buses."
else:
    print "Fine, let's stay home then."

print "cars < people is: %r" % (cars < people)  # 自己加的
