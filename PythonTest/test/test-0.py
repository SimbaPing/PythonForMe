print('{0:.3f}'.format(1.0/3))
print('a', end='')
print('b', end='')
print('c')
print(r"Newlines are indicated by \n")

# while True:
#     s = input("Enter something: ")
#     if s == "quit":
#         break
#     if len(s) < 3:
#         print("Too small")
#         continue
#     print("Input is of sufficient length")


def say_hello():
    print("hello world!")


say_hello()


def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")


print_max(3, 4)

x = 50


def func(x):
    print("x is", x)
    x = 2
    print("Changed local x to", x)


func(x)
print("x is stall", x)


def total(a=5, *numbers, **phonebook):
    '''
    Look at me.
    '''
    print("a", a)

    for single_item in numbers:
        print("single_item", single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
