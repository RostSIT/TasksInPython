a = int(input())+1
while len(set(str(a))) != len(str(a)):
    a += 1
print(a)
