"""Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.



Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это
латинские буквы abcdefgh, а строки это символы цифр от 1-8

Разбор Youtube Patreon Boosty

Sample Input 1:

a1
b2
Sample Output 1:

YES
Sample Input 2:

f5
c3
Sample Output 2:

NO
"""

a = '_abcdefgh'
coord1 = input()
coord2 = input()

letter1 = coord1[0]
letter2 = coord2[0]
column1 = a.find(letter1)
column2 = a.find(letter2)
row1 = int(coord1[1])
row2 = int(coord2[1])

if (column1 + row1) % 2 == (column2 + row2) % 2:
    print('YES')
else:
    print('NO')


