"""
6.5 Множества в Python. Тип данных set
1 из 11 шагов пройден
0 из 24 баллов  получено
Даны два списка чисел.

Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

Sample Input:

1 3 2 5
4 3 2 6
Sample Output:

2 3
"""

a = set(map(int, input().split()))
b = set(map(int, input().split()))

for i in sorted(a & b):
    print(i, end=' ')
