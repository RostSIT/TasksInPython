"""
6.5 Множества в Python. Тип данных set
1 из 11 шагов
"""

# create
a = {1, 2, 3, 4}
print(a, type(a))
print()

a1 = {1, 2, 3, 4, 1, 2, 3}
print(a1, type(a1))
print()

b = {'hi', 'ha', 'hi', 'hi'}
print(b, type(b))
print()

c = set('abracadabra')
print(c, type(c))
print()

e = set(range(5))
print(e, type(e))
print()

f = {}
print(f, type(f))
print()

a = {1, 2, 3, 4, 1, 2, 3}
a = list(set(a))
print(a)
print()

a = {1, 2, 3, 4, 1, 2, 3}
a.add(0)
print(a)

a.add(1)
a.add(4)
print(a)
print()

a.update([5, 6, 7])
print(a)

a.update([0, 0, 1, 1, ])
print(a)
print()

a.update('hello')
print(a)
print()

a.update(range(-3, 3))
print(a)
print()

a.update({11, 44, 55, 'k'})
print(a)
print()

a.discard(55)
print(a)
a.discard(55)
print(a)
print()

a.remove(44)
print(a)
# a.remove(44)
# print(a)
print()

print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print()

print(a)
a.clear()
print(a)
print()

a = {11, 44, 55, 'k'}

print(len(a))
print(a)
print()

print(-1 in a, 7 in a, 7 not in a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
c = {10, 11, 12}
print(a & b)
print(a & c)
print(a, b, c)
print()

a &= c
print(a)
a = {4, 3, 2, 1}
a &= b
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
c = {10, 11, 12}
print()

print(a.intersection(b))  # a & b
print('a & b ==', a & b)
print()

print(a, b)
a.intersection_update(b)  # a& = b
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
print(a | b)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
print(a.union(b))  # a | b
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
a = a.union(b)  # a | b
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
a |= b  # a | b
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
print('a - b ==', a - b)
print(a)
print()

print(a, b)
print('b - a ==', b - a)
print(b)
print()

print(a, b)
b -= a  # b - a
print(b)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
print('a ^ b ==', a ^ b)
print(a)
print()

print(a, b)
print('b ^ a ==', b ^ a)
print(a)
print()

print(a, b)
a ^= b  # b ^ a
print(a)
print()

a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}

print(a, b)
print('a == b ==', a == b)

a = {4, 3, 2, 1}
b = {3, 4, 4, 3, 1, 1, 2}

print(a, b)
print('a == b ==', a == b)

a = {4, 3, 2, 1}
b = {1, 2, 3}
print(a, b)
print(a < b)
print(a > b)
print()

a = {4, 3, 2, 1}
b = {1, 2, 5}
print(a, b)
print(a < b)
print(a > b)
print()

a = {4, 3, 2, 1}
b = {1, 2, 3, 4}
print(a, b)
print(a >= b)
print()

for i in a:
    print(i)  # not index (print(a[1])

# exemple
text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    text = input()
print(len(a))
