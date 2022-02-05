"""
5.6 Вложенные списки
11 из 16 шагов пройдено
53 из 87 баллов  получено
Состязания - 3

В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого
максимален наилучший бросок. Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по
всем попыткам. Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер
победителя соревнований.

Входные данные

Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке
идет n строк по m чисел, являющихся элементами массива.

Выходные данные

Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены)
нумеруются с 0.

Решение задачи Youtube Patreon Boosty

Sample Input:

3 3
1 2 7
1 3 5
4 1 6
Sample Output:

0
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

max_score = 0
max_summa = 0
max_index = 0
for row in range(n):
    max_try = 0
    s = 0
    for column in range(m):
        s += a[row][column]
        if a[row][column] > max_try:
            max_try = a[row][column]

    if max_try > max_score:
        max_score = max_try
        max_summa = s
        max_index = row
    elif max_try == max_score and s > max_summa:
        max_score = max_try
        max_summa = s
        max_index = row
print(max_index)

