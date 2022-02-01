"""
Найдите сумму всех четырехзначных чисел,
сумма цифр каждого из которых равна 20.
"""

count = 0

for i in range(1000, 10000):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    if s == 20:
        count += i
        print(i, s)
print(count)
