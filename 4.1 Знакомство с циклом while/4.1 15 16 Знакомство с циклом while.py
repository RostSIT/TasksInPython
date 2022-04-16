# a = int(input())
# count = 0
# while a > 1:
#     if a % 2 != 0:
#         count = "НЕТ"
#         break
#     else:
#         a /= 2
#         count += 1
# print(count)

a = int(input())
count = 0
while a >= 1 and a % 2 == 0:
    a /= 2
    count += 1
print(count if a == 1 else 'НЕТ')

"""В архитектуре компьютера важную роль играют числа, являющиеся степенями двойки: 1, 2, 4, 8 и так далее. Напишите
программу, которая проверяет, является ли введённое натуральное число степенью двойки. Если да, то выводится сама эта
степень; если нет, выводится «НЕТ»

Разбор Youtube Patreon Boosty

Sample Input 1:

8
Sample Output 1:

3
Sample Input 2:

9
Sample Output 2:

НЕТ"""
