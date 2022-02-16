"""

"""

a = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Gordachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Vukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006),
]

print([elem[0] for elem in a if elem[0].startswith('E')])
print(1)
print()

print([elem[0] for elem in a if elem[1] > 2000])
print(2)
print()



a = {
    'Sidorov':{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov':{'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov':{'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gordachev':{'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin':{'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev':{'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev':{'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov':{'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov':{'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
print([elem for elem in a])
print('4a')
print()

print([a[elem]['car'] for elem in a])
print('4b')
print()

print([a[elem]['hobby'] for elem in a])
print('4c')
print()

print([(elem, a[elem]['car']) for elem in a
       if a[elem]['age'] < 2000])
print('4d')
print()

print([(elem, a[elem]['car']) for elem in a if a[elem]['age']
       < 2000 and a[elem]['hobby'] == 'soccer'])
print('4i')
print()

s = 'abc543qwERty32454><^@hRe321'
print([i for i in s if i.isalpha()])
print()

print([int(i) for i in s if i.isdigit()])
print()

print([int(i) for i in s if i.isdigit()])
print('Возвращает числа')
print()

print(3)
print()

import random

n = 7
m = 7

a = [[random.randint(1, 6) for j in range(m)]
     for i in range(n)]
print('Содержимое матрицы:')
for i in a:
    print(i)

# главная диагональ
b = [a[i][j] for i in range(n)
     for j in range(m) if i == j]
print('главная диагональ')
print(b)
# 2 строка (нурмерация с 0)
с = [a[2][j] for j in range(m)]
print('2 строка матрицы')
print(с)
# 3 столбец (нурмерация с 0)
d = [a[i][3] for i in range(n)]
print('3 столбец матрицы')
print(d)
print(4)
print()

n = 5
m = 5
a = [[i * j for j in range(1, m + 1)]
     for i in range(1, n + 1)]
for i in a:
    print(i)
print(5)
print()

print(6)
print()
