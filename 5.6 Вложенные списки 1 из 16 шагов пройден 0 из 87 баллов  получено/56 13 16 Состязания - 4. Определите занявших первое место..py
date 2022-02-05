"""
5.6 Вложенные списки
12 из 16 шагов пройдено
60 из 87 баллов  получено
Состязания - 4

В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победитель определяется по лучшему
результату. Определите количество участников состязаний, которые разделили первое место, то есть определите
количество строк в массиве, которые содержат значение, равное наибольшему.

Входные данные

Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке
идет n строк по m чисел, являющихся элементами массива.

Выходные данные

Программа должна вывести  одно число - количество победителей соревнования.

Разбор Youtube Patreon Boosty

Sample Input 1:

3 3
3 1 2
1 3 4
4 3 3
Sample Output 1:

2
Sample Input 2:

4 3
7 8 9
9 3 10
4 3 8
5 6 7
Sample Output 2:

1
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
maximum = 0
count = 0

for i in range(n):
    local_maximum = 0
    for j in range(m):
        if a[i][j] > local_maximum:
            local_maximum = a[i][j]
    if local_maximum > maximum:
        maximum = local_maximum
        count = 1
    elif local_maximum == maximum:
        count += 1
print(count)
