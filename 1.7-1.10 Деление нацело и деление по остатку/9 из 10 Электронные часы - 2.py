'''
1.7 Деление нацело и деление по остатку
9 из 10 шагов пройдено
16 из 20 баллов  получено
Электронные часы - 2

Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

Программа получает на вход число n - количество секунд, которое прошло с начала суток.

Выведите показания часов, соблюдая формат.

Разбор решения Youtube Patreon Boosty

Sample Input 1:

3721
Sample Output 1:

1:02:01
Sample Input 2:

5000
Sample Output 2:

1:23:20
'''
# Моя попытка
timeInSeconds = int(input())

hours = timeInSeconds % 86400 // 3600
minutes = timeInSeconds % 86400 % 3600 // 60
seconds = timeInSeconds % 86400 % 3600 % 60

minutes0 = ""
seconds0 = ""

if minutes <= 9:
    minutes0 = 0

if seconds <= 9:
    seconds0 = 0

print(f'{hours}:{minutes0}{minutes}:{seconds0}{seconds}')

# Разбор Егорова
timeInSeconds = int(input())
hours = (timeInSeconds // 3600) % 24
timeInSeconds = timeInSeconds % 3600
minutes = timeInSeconds // 60
timeInSeconds = timeInSeconds % 60
seconds = timeInSeconds

print(hours, ':', minutes // 10, minutes % 10, ':', seconds // 10, seconds % 10, sep='')
