"""
5.5 Вложенные циклы
4 из 8 шагов пройдено
11 из 35 баллов  получено
Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.

Формат ввода
Несколько натуральных чисел на одной строке.

Формат вывода
Несколько чисел на одной строке.

Sample Input:

3 7 1 10 8
Sample Output:

***
*******
*
**********
********
"""

[print(int(i) * "*") for i in input().split()]
# for i in map(int, input().split()):
#     print('*'*i)

