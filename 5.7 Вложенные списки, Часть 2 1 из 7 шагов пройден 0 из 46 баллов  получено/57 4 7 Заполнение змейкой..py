"""
5.7 Вложенные списки, Часть 2
3 из 7 шагов пройдено
15 из 46 баллов  получено
Заполнение змейкой

Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

Sample Input:

4 10
Sample Output:

0  1  2  3  4  5  6  7  8  9
19 18 17 16 15 14 13 12 11 10
20 21 22 23 24 25 26 27 28 29
39 38 37 36 35 34 33 32 31 30
"""

n, m = map(int, input().split())
mas = []
for i in range(n):
    mas.append([0] * m)
# print(mas)
count = 0
ten = 10
counter = 0
# for i in mas:
#     print(i)
for i in range(n):
    for j in range(m):
        mas[i][j] += count
        if mas[i][j] < 10:
            print(mas[i][j], end='  ')
        else:
            print(mas[i][j], end=' ')
        count += 1

    print()
    counter += 1
    if counter == n:
        break
    for j in range(m - 1, -1, -1):
        mas[i][j] += ten
        print(mas[i][j], end=' ')
        count += 1
    counter += 1
    if counter == n:
        break
    print()
