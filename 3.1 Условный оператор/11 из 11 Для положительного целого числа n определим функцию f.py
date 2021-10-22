"""
3.1 Условный оператор
10 из 11 шагов пройдено
21 из 25 баллов  получен
Для положительного целого числа n определим функцию f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Ваша задача — посчитать f(n) для данного целого числа n.

В единственной строке записано положительное целое число n (1 ≤ n ≤ 1015).

Выведите f(n) в единственной строке.

Примечание

f(4) =  - 1 + 2 - 3 + 4 = 2

f(5) =  - 1 + 2 - 3 + 4 - 5 =  - 3

Разбор решения Youtube Patreon Boosty

Оригинал задачи http://codeforces.com/problemset/problem/486/A

Sample Input 1:

4
Sample Output 1:

2
Sample Input 2:

5
Sample Output 2:

-3
"""

# It's my example.
n = int(input())

def f(n):
    c = 0
    a = range(n)
    for i in a:
        i += 1
        if i % 2 == 0:
            c += i
        else:
            c -= i
    print(c)


f(n)

###################################################

# It's not my example.
n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    print(n // 2 - n)






