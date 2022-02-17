def find_duplicate(a):
    b = []
    for i in a:
        if a.count(i) > 1 and i not in b:
            b.append(i)
    return b


a = [1, 1, 3, 3, 4, 5, 66, 66]
print(find_duplicate(a))
