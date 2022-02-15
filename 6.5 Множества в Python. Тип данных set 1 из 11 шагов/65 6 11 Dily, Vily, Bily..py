a = input()
b = {}
while a == 'конец':
    a = input()
    b.setdefault(a)

print(b)
