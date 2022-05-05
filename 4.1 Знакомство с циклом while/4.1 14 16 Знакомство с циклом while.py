a, b = map(int, input().split())
hour = 0
while a - hour + hour//b > 0:
    hour += 1
print(hour)

#