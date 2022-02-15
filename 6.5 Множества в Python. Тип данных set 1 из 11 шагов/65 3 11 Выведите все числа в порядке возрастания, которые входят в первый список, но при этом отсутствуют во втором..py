"""
6.5 Множества в Python. Тип данных set
2 из 11 шагов пройдено
1 из 24 баллов  получен
Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором.

Sample Input:

1 3 2 5
4 3 2 6
Sample Output:

1 5
"""

a = set(map(int, input().split()))
b = set(map(int, input().split()))
for i in sorted(a - b):
    print(i, end=' ')
# print(set(i for i in sorted(set(map(int, input().split()))-set(map(int, input().split())))))
