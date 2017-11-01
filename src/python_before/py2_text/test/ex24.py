# -*- coding:utf-8 -*-

print "Let's practice everything."  # 让我们实践一切
# 这段很长    \    \\    \n    \t    用法
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# 这是一首诗歌
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an esplanation
\n\t\twhere there is none.
"""

print "-----------------"
print poem
print "-----------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five  # 格式化字符串


def sercet_formula(started):  # 密码 公式 出发
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = sercet_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % sercet_formula(start_point)
