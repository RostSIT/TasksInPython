# [выражение for val in коллекция]

# [выражение for val in коллекция if условие]

a = [i for i in range(10)]
print(a)
print(1)
print()

a = [i ** 2 for i in range(1, 15)]
print(a)
print(2)
print()

a = [i % 4 for i in range(1, 15)]
print(a)
print(3)
print()

a = [i * 5 for i in 'fello']
print(a)
print(4)
print()

a = [ord(i) for i in 'fello']
print(a)
print(5)
print()

import random

a = [random.randint(-10, 10) for i in 'fello']
print(a)

b = [abs(elem) for elem in a]
print(b)
print()

a = [elem + 1 for elem in a]
print(a)
print()

b = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0]
print(b)
print(6)
print()

a = input().split()
a = [int(i) for i in a]
print(a)
print(7)
print()

n = 5
m = 4
a = [[0] * m for i in range(n)]
a[1][3] = 100
for i in a:
    print(i)
print(8)
print()

a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)
print(9)
print()

a = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j > 10]
print(a)
print(10)





