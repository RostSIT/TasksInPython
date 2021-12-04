"""
4.4 Алгоритм Евклида
4 из 4 шагов пройдено
3 из 3 баллов  получено
Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).

Sample Input 1:

6 15
Sample Output 1:

30
Sample Input 2:

14 21
Sample Output 2:

42
"""

a, b = map(int, input().split())
c = a * b
while b > 0:
    a, b = b, a % b
d = c / a
print(int(d))

