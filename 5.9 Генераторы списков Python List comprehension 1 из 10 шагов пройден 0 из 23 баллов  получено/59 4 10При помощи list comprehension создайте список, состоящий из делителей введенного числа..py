"""
При помощи list comprehension создайте список, состоящий из делителей введенного числа.

"""

n = int(input())
a = [i for i in range(1, n+1) if n % i == 0]
print(a)

