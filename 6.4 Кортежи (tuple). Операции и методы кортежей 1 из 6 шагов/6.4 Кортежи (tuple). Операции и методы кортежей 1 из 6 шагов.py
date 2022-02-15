"""
6.4 Кортежи (tuple). Операции и методы кортежей
1 из 6 шагов
"""
# кортеж - неизменяемый объект
a = tuple()
print(a, type(a))
print()

a = ()
print(a, type(a))
print()

a = (1, 2, 3, 4, 5)
print(a, type(a))
print()

a = 1, 2, 3, 4
print(a, type(a))
print()

a = 1,
print(a, type(a))
print()

a = tuple(range(5))
print(a, type(a))
print()

a = tuple([1, 2, 3])
print('a = tuple([1, 2, 3]) ==', a, type(a))
print()

b = tuple((1, 2, 3, 4))
print(b, type(b))
print()

print('b = 1, 2, 3, 4', ' len(b) ==', len(b), ', ''2 in b ==',
      2 in b, ', ''6 in b ==', 6 in b, ' 6 not in b ==', 6 not in b)
print()

print('a + b ==', a + b)
print()

print('b + a ==', b + a)
print()

print(b * 3)
print()

print('max(b), min(b) ==', max(b), ',', min(b),
      ' # values of the same type')  # values of the same type
print()

print('sum(b) ==', sum(b),
      ' # values of the same type')  # values of the same type
print()

a = (1, 'hello', False, 4)
print(f'a = (1,"'"hello"'", False, 4), a[2] ==', a[2])
print()

# кортеж - неизменяемый объект


a = tuple([1, 'hello', [10, 20, 30], False, 4])
b = [1, 'hello', [10, 20, 30], False, 4]
c = ([1, 'hello', [10, 20, 30], False, 4])

print(type(a), 'размер кортежа a = \n tuple([1, '"'hello'"', '
               '[10, 20, 30], False, 4]) равен:', a.__sizeof__(), 'byte')
print()

print(type(b), 'размер списка a = \n [1, '"'hello'"', '
               '[10, 20, 30], False, 4] равен:', b.__sizeof__(), 'byte')
print()

print(type(c), 'размер списка a = \n ([1, '"'hello'"', '
               '[10, 20, 30], False, 4]) равен:', c.__sizeof__(), 'byte')
print()

print('a = tuple([1, '"'hello'"', '
      '[10, 20, 30], False, 4]), a.index(1) ==', a.index(1))
print('a = tuple([1, '"'hello'"', '
      '[10, 20, 30], False, 4]), a.count(4) ==', a.count(4))
print('a = tuple([1, '"'hello'"', '
      '[10, 20, 30], False, 4]), a.count(4) ==', a.count(6))
print()

# изменяются, изменяемые объекты в кортеже, но не сам кортеж
a[2].append(100)
print('a = tuple([1, '"'hello'"', '
      '[10, 20, 30], False, 4]), a.[3]append(100)] ==', '\n', a,
      '\n# изменяются, изменяемые объекты в кортеже, но не сам кортеж')
print()

# можно использовать кортеж, как ключ в словаре
a = (1, 2, 3)
b = {}
b[a] = 'hello'
print('a = (1, 2, 3), b = {}, b[a] = "'"hello"'"',
      '\n', b, '  # можно использовать кортеж, как ключ в словаре')
print()

# можно изменять кортеж с помощью списка.
a = (1, 2, 3)
a = list(a)
a.append(200)
a.reverse()
a = tuple(a)
print(a, type(a), '# можно изменять кортеж с помощью списка.')
print()

a = (1, 2, 3)
for i in a:
    print(i)
print()

for i in range(len(a)):
    print(a[i])



