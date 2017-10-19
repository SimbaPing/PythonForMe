import keyword

print("Hello world!")

var = keyword.kwlist
print(var)
print('*' * 36)
print('*' * 10 + "基本数据类型，六种" + '*' * 10)
'''1.Numbers'''
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
'''2.String'''
s = 'Yes, he doesn\'t'
print(s, type(s), len(s))
'''3.List'''
a = ['him', 26, 100, 'her']
print(a)
var = a + ['he', 22, 10]
print(var)
'''4.Tuple'''
a = (111, 222, 333, 'good')
print(a, type(a), len(a))
'''5.Sets'''
a = {'Tom', 'Jim', 'John'}
print(a)
a = set('asdfgdfgdg')
b = set('asgsdae')
print(a)
print(b)
'''6.Dictionaries'''
dic = {}
tel = {'Jack': 1557, 'Tom': 1320, 'John': 1888}
print(tel)
print('*' * 36)


def return_me(a, b):
    c = a + b
    return c


print(return_me(3, 5))
