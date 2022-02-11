"""6.1 Словари Python. Операции и методы словаря 3 из 6 шагов пройдено 8 из 14 баллов  получено Напишите программу,
которая печатает словарь alphabet, где ключи  - строчные английские символы, а значения - порядковые номера букв в
алфавите.

Начало вашего словаря должны быть таким {"a": 1, "b": 2 }

В качестве ответа распечатайте ключи и значения данного словаря по алфавиту, каждую пару на новой строчке.

Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:

from string import ascii_lowercase
print(ascii_lowercase)
Sample Input:

Sample Output:

a 1
b 2
c 3
d 4
e 5
f 6
g 7
h 8
i 9
j 10
k 11
l 12
m 13
n 14
o 15
p 16
q 17
r 18
s 19
t 20
u 21
v 22
w 23
x 24
y 25
z 26
"""

from string import ascii_lowercase

alphabet = {}
for i in range(26):
    b = ascii_lowercase[i]
    alphabet.setdefault(b, i+1)
# print(alphabet)
# alphabet.items()
for key in alphabet:
    print(key, alphabet[key])