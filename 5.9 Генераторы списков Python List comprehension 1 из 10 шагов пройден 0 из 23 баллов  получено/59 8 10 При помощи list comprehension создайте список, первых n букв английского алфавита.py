"""
5.9 Генераторы списков Python | List comprehension
7 из 10 шагов пройдено
15 из 23 баллов  получено
При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...]. Получить все заглавные буквы английского алфавита можно следующим образом:

from string import ascii_uppercase
print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
Входные данные
На вход программе подается натуральное число n, n≤26.

Формат выходных данных
Программа должна вывести список из первых n заглавных букв английского алфавита

Sample Input 1:

3
Sample Output 1:

['A', 'B', 'C']
Sample Input 2:

5
Sample Output 2:

['A', 'B', 'C', 'D', 'E']
Sample Input 3:

9
Sample Output 3:

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
"""

from string import ascii_uppercase
# print(ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

n = int(input())
print([ascii_uppercase[i] for i in range(n)])
# print([chr(a[i]) for i in range(n)])

