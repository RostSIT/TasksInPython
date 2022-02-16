import string

alphabet = set(string.ascii_uppercase)
a = int(input())
b = set(input().upper())
if b == alphabet:
    print('YES')
else:
    print('NO')
