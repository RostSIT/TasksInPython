from math import gcd
from functools import reduce

a = int(input())
b = [int(input()) for i in range(a)]


def find_gcd(list):
    x = reduce(gcd, list)
    return x


print(find_gcd(b))

# import math
# A = [12, 24, 27, 30, 36]
# print(math.gcd(*A))

n = int(input())
lst = [int(input()) for i in range(n)]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


s = []
for i in range(len(lst)):
    for j in range(len(lst)):
        s.append(gcd(lst[i], lst[j]))
print(min(s))

"""7.3 Возвращаемое значение функции. Оператор return
3 из 8 шагов пройдено
2 из 18 баллов  получено
Снова НОД
В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольших общий делитель для них.

Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.

Входные данные
На первой строке вводится натуральное число n – количество чисел. Далее идут n строк, в каждой из которых натуральное число.

Входные данные
НОД введенных чисел.

Sample Input 1:

3
15
18
27
Sample Output 1:

3
Sample Input 2:

4
24
60
48
12
Sample Output 2:

12"""