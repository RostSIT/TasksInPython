a = list(map(int, input().split()))
b = []

if max(a) <= 0:
    print("Empty")
else:
    for i in a:
        if i > 0:
            b.append(i)
    print(min(b))

print((sorted([i for i in map(int, input().split()) if i > 0]) + ['Empty'])[0])

nums = [i for i in map(int, input().split()) if i > 0]
if nums:
    print(min(nums))
else:
    print('Empty')
"""На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. В случае, если положительных значений нет, выведите строку "Empty"

Sample Input 1:

8 11 -9 0 5 -20
Sample Output 1:

58 11 -9 0 5 -20

Sample Input 2:

5 -2 -1 18 4 -6
Sample Output 2:

4
Sample Input 3:

-4 -7 0 -19
Sample Output 3:

Empty"""
