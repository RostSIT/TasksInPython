"""6.2 Ситуации, где полезно использовать словарь 2 из 5 шагов пройдено 1 из 7 баллов  получен В этой задаче вам
предстоит достать определенные данные из словаря data. Он уже будет определен и заполнен данными, поэтому никакого
ввода значений в это программе делать не нужно, просто обращаетесь к переменной data

У словаря data следующая структура ключей

{ "my_friends": { "count": ..., "items": [ { "first_name": value, "id": value, "last_name": value, }, { "first_name":
value, "id": value, "last_name": value, }, ...... ] } } Ваша задача получить значения ключа first_name у всех
элементов и вывести их в алфавитном порядке, каждое имя с новой строки

P.S. Если стало уж совсем трудно и непонятно, воспользуйтесь следующим:

print(data)
"""

data = {'my_friends':
            {'count': 10, 'items':
                [{'first_name': 'Kurt',
                  'id': 621547005,
                  'last_name': 'Cobain',
                  'bdate': '31.8.2005'},
                 {'first_name': 'Виолетта',
                  'id': 484200150,
                  'last_name': 'Кастилио'},
                 {'first_name': 'Иринка',
                  'id': 21886133,
                  'last_name': 'Бушуева',
                  'bdate': '28.8.1942'},
                 {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
                 {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
                 {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин', 'bdate': '6.12.1982'},
                 {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова', 'bdate': '4.11.1995'},
                 {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
                 {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
                 {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова', 'bdate': '20.12'}]}}

persons = ['my_friends']

counter = 0
d = {}
a = {}
for person in persons:
    # print(person, data[person]['items'][counter])

    for i in data[person]['items']:
        for j in data[person]['items'][1]:
            # print(data[person]['items'][counter][j])
            d.setdefault(data[person]['items'][counter][j])
        # print(data[person]['items'][counter])
        # a = data.get('first_name')
        # f.setdefault(i)
        # print(a)
        counter += 1
# for i in sorted(d):
#     print(i, d[i])


print(d)
