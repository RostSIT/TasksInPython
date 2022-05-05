s = input().lower()
count1 = []
for i in range(len(s) - 1):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
            count1.append(count)
print(max(count1))

word = input().lower()
print(max([word.count(i) for i in word]))
