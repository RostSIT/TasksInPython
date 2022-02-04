

n = int(input())
a = list(map(int, input().split()))
N = len(a)
count = 0
for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            count += 1
        else:
            break
print(*a)
print(count)
