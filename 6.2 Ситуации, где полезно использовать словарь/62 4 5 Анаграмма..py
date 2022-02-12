"""
6.2 Ситуации, где полезно использовать словарь
2 из 5 шагов пройдено
1 из 7 баллов  получен
Анаграмма
Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.

Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

Sample Input 1:

abc
cba
Sample Output 1:

YES
Sample Input 2:

abracadabra
cadabraabra
Sample Output 2:

YES
Sample Input 3:

abb
bbc
Sample Output 3:

NO
"""

a = []
b = []
S1 = input()
S2 = input()
for i in sorted(S1):
    a.append(i)

for i in sorted(S2):
    b.append(i)
if a == b:
    print('YES')
else:
    print('NO')
