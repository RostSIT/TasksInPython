"""
Сортировка подсчетом

Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до
100 включительно, сортировкой подсчетом.

Программа получает на вход число n - количество элементов в списке, затем сами элементы списка

Вам необходимо вывести отсортированный список

P.S. не пользуйтесь встроенной функцией sorted или методом sort

Sample Input 1:

5
8 9 8 7 2
Sample Output 1:

2 7 8 8 9
Sample Input 2:

7
-8 5 -7 4 -8 0 4
Sample Output 2:

-8 -8 -7 0 4 4 5
Sample Input 3:

8
66 -66 -48 -96 -17 -80 -57 -45
Sample Output 3:

-96 -80 -66 -57 -48 -45 -17 66
"""

n = int(input())
a = list(input().split())
count = [0] * 201
# import random
# for i in range(n):
#     a.append(random.randint(-100, 100))

# count = [0] * (max(a) - min(a) + 1)

for i in a:
    count[int(i) + 100] += 1
# print(count)
for i in range(201):
    if count[int(i)] > 0:
        print((str(int(i) - 100) + ' ') * count[i], end='')


# count = [0] * 201
# for i in a:
#     count[i + 100] += 1
# print(a)
# for i in range(201):
#     if count[i] > 0:
#         print(i - 100, count[i])


