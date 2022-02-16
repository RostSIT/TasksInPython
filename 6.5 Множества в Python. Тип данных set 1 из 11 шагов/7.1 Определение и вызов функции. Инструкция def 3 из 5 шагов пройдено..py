# определение функции
def seyHello():  # функция без аргументов
    print('hello')
    print('world')
    print('and everybody')


seyHello()


def square(x):
    print('Квадрат числа', x, '=', x ** 2)  # функция с одним аргументом


square(5)


def multiply(a, b):  # функция с двумя аргументами
    print(a * b)


multiply(2, 3)


def even(a):
    if a % 2 == 0:
        print(a, '')
    else:
        print(a, '')


# главная программа (в ней вызывают фуекцию)
for i in range(20, 31):
    even(i)


def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)


factorial(5)

if 5 > 1:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')
primer()
