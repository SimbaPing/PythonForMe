"""Created with IntelliJ by Django on 2020/11/22 1:35"""


for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print(i, 'equals', x, '*', i//x)
            break
    else:
        print(i, 'is a prime number')

for i in range(2, 10):
    if i % 2 == 0:
        print('Found an even number', i)
        continue
    print('Found an odd number', i)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in('y', 'ye', 'yes',):
            return True
        if ok in ('n', 'no', 'nop', 'nope',):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


print(ask_ok('Do you really want to quit?'))
print(ask_ok('OK to overwrite the file?', 2))
