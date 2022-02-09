"""
5.9 Генераторы списков Python | List comprehension
7 из 10 шагов пройдено
13 из 23 баллов  получено
Создайте список первых букв каждого слова из строки st и выведите его на экран
"""
st = 'Create a list of the first letters of every word in this string'

Firstletters = []
for i in st.split():
    Firstletters += i[0]
print(Firstletters)

# print([Firstletters.append(i) for i in st.split() if i[0]])

