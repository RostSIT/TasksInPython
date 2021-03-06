comments = {
    'Дили': set(),
    'Вили': set(),
    'Били': set(),
}
a = input()
while a != 'конец':
    name, commentator = a.split(': ')
    comments[name].add(commentator)
    a = input()

for k, v in sorted(comments.items(), key=lambda item: -len(item[1])):
    print(f'Количество уникальных комментаторов у {k} - {len(v)}')

"""
6.5 Множества в Python. Тип данных set
6 из 11 шагов пройдено
8 из 24 баллов  получено
Дили Вили Били завели себе аккаунты в одной известной соцсети. И затем они решили узнать у кого из них самое большое количество уникальных комментатор. Ваша задача помочь им в этом и собрать нужную информацию.

Входные данные
В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора. Комментаторы могут повторяться и комментировать разных персонажей

Строка "конец" означает окончание ввода и встречается последней

Входные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать обращать внимания в этой задаче.

Гарантируется, что количество уникальных комментаторов у всех наших героев разное. Могут быть ситуации, когда у героя нету ни единого комментатора, в таком случае все равно нужно выводить информацию о нем.

Sample Input 1:

Дили: navalny
Дили: realdonaldtrump
Били: navalny
Вили: realdonaldtrump
Вили: realdonaldtrump
Били: joebiden
Дили: joebiden
конец
Sample Output 1:

Количество уникальных комментаторов у Дили - 3
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Вили - 1
Sample Input 2:

Дили: aaaa
Дили: aaaa
Били: aaaa
Дили: aaaa
Били: aaa
конец
Sample Output 2:

Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Дили - 1
Количество уникальных комментаторов у Вили - 0
"""
