# В данном занятии разберем как при помощи цикла while можно обойти все цифра числа

x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
maxim = 0
minim = 9

while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    pr = pr * last
    if last > maxim:
        maxim = last
    if last < minim:
        minim = last
    x = x // 10

print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', s)
print('Произведение всех цифр:', pr)
print('Maxim:', maxim)
print('Minim:', minim)

x = int(input())
while x > 0:
    last = x % 5
    print(last)
    x = x // 2  # Перевод в двоичную систему.
