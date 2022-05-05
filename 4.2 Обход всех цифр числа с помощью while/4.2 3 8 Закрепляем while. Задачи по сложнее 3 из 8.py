# put your python code here
n = int(input())
a = []
count = 0
while sum(a) <= n:
    a.append(int(input()))
    if sum(a) <= n:
        count += 1
print(f'Довольно!\n{sum(a[:-1])}\n{count}')
