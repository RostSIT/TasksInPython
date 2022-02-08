n = int(input())
mas = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0:
            mas[i][j] = 1
        else:
            mas[i][j] = 0

        print(mas[i][j], end=' ')
    print()
for i in range(n, 1, 1):
    for j in range(n):
        if mas[i - 1][j] > 0 and mas[i][j + 1] > 0:
            print()
            mas[i][j] = mas[i - 1][j] + mas[i][j + 1] > 0
            print(mas[i][j], end=' ')
        else:
            mas[i][j] = 0
            print(mas[i][j], end=' ')
        print()
