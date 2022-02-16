a = int(input())+1
while len(set(str(a))) != len(str(a)):
    a += 1
print(a)

"""
6.5 Множества в Python. Тип данных set
9 из 11 шагов пройдено
20 из 24 баллов  получено
Красивый год
Кажется, еще совсем недавно наступил новый 2013 год. А знали ли Вы забавный факт о том, что 2013 год является первым годом после далекого 1987 года, в котором все цифры различны?

Теперь же Вам предлагается решить следующую задачу: задан номер года, найдите наименьший номер года, который строго больше заданного и в котором все цифры различны.

Входные данные
В единственной строке задано целое число y (1000 ≤ y ≤ 9000) — номер года.

Выходные данные
Выведите единственное целое число — минимальный номер года, который строго больше y, в котором все цифры различны. Гарантируется, что ответ существует.

Sample Input 1:

1987
Sample Output 1:

2013
Sample Input 2:

2013
Sample Output 2:

2014
"""