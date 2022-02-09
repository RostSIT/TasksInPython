"""
При помощи list comprehension создайте список, состоящий из делителей введенного числа.

"""

n = int(input())
print([i for i in range(1, n+1) if n % i == 0])


