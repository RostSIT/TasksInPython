a = list(input())
b = []
count = 0
for i in a:
    if i.isdigit():
        count += 1
        b.append(int(i))
print(f'{count} {sum(b)}')


x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t.append("4")
s=s+"4"


print(str(x) + " " + s)