def factorial(a):
    pr = 1
    for i in range(2, a + 1):
        pr *= i
    return pr


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def factorial(a):
    pr = 1
    for i in range(2, a + 1):
        pr *= i
    return pr


print(factorial(4))

"""7.3 Возвращаемое значение функции. Оператор return 1 из 8 шагов пройден 0 из 18 баллов  получено Напишите функцию 
factorial, которая принимает на вход одно неотрицательное число, и возвращает значение факториала данного числа. 

Нужно определить только функцию

Sample Input 1:

4
Sample Output 1:

24
Sample Input 2:

5
Sample Output 2:

120"""
