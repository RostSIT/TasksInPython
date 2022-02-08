n = int(input())

triangle = []
for i in range(n):
    triangle.append([1] + [0]*(n-1))
for i in triangle:
    print(i)
print()
for i in range(1, n):
    for j in range(1, i+1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in range(0, n):
    for j in range(0, i+1):
        print(triangle[i][j], end=' ')
    print()
