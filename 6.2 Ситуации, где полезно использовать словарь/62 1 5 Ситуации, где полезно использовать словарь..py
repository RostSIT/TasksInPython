"""
4 Ситуации, где полезно использовать словарь
"""
print('№I. ПОДСЧЕТ КОЛИЧЕСТВА ОБЪЕКТОВ')

d = {}
d['a'] = 1
print(d)
if 'a' in d:
    d['a'] = 1
else:
    d['a'] = 1
print(d)
print('№1______________________________________')
print()

# s = input()
s = 'poiiiuyyy222133'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
print('№2______________________________________')
print()

# s = input()
s = 'poiiiuyyy222133'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(i, d[i])
print('№3______________________________________')
print()

s = 'poiiiuyyy222133222133'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in sorted(d):  # сортировка по алфавиту.
    print(i, d[i])
print('№4______________________________________')
print()

s = 'poiiiuyyy222133'
d = {}
for i in s:
    if i.isalpha():  # вывести только буквы.
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
for i in sorted(d):  # сортировка по алфавиту.
    print(i, d[i])
print('№5==============================================')
print('№I==============================================')

print()

print('№II. ЗАМЕНА РАЗРЯЖЕННОГО СПИСКА')
print()
s = 'poiiiuyyy222133'
letters = [0] * 26
for i in s.lower():
    if i.isalpha():
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:  # вывод значений больше нуля
        print(chr(i + 97), letters[i])
print('№II.1______________________________________')
print()

s = 'poiiiuyyy222133'
letters = [0] * 26
for i in s.lower():
    if i.isalpha():
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(26):
    # if letters[i] > 0:  # вывод значений больше нуля
    print(chr(i + 97), letters[i])
print('______Разряженны список')
print('№II.2______________________________________')
print()

s = 'poiiiuyyy222133'
letters = [0] * 26
for i in s.lower():
    if i.isalpha():
        nomer = ord(i) - 97
        letters[nomer] += 1
print('Разряженны список:', '\n', letters)

# for i in range(26):
#     # if letters[i] > 0:  # вывод значений больше нуля
#         print(chr(i + 97), letters[i])
print('№II.3 ______________________________________')
print()

s = 'poiiiuyyy222133'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)
print('№II.4 ______________________________________')
print('№II.==============================================')
print()

print('№III. УСТАНОВИТЬ СООТВЕТСТВИЕ МЕЖДУ ОБЪЕКТАМ')
print()

words = {}
while True:
    s = input()
    if s in words:
        print('Словов', s, 'переводиться как', words[s])
    else:
        print('Введите перевод слова', s)
        words[s] = input()
print('№III.==============================================')

print('№IV. ХРАНАНИЕ ДАННЫХ ОБ ОБЪЕКТЕ')
print('№IV.==============================================')
