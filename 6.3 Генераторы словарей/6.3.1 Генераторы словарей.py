"""
Генераторы словарей Python | Dictionary comprehension python
"""

# key: value
print('# key: value')
a = {i: i ** 2 for i in range(1, 11)}
print(a)
print()

# без генератора словарей
print('# без генератора словарей')
a = {}
for i in range(1, 11):
    a[i] = i ** 2
print(a)
print()

# вариант гениратора словаря строк
print('# вариант гениратора словаря строк')
a = {word: len(word) for word in ['hello', ' hi', ' www']}
print(a)
print()

data = {
    'Amy SmiTh': '694',
    'Brian ShAw': '593',
    'christian Sharp': '118',
    'Sean Schmidt': '972',
}
new_data = {key.title(): int(value) for key, value in data.items()}
print(data)
print(new_data)
print()

# без генератора словарей
print('# без генератора словарей')
new_data = {}
for key, value in data.items():
    new_data[key.title()] = int(value)
print(data)
print(new_data)
print()

users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [51, 'qwerty', '1234'],
]
new_users = {user[0]: user for user in users}
print(new_users[51])
