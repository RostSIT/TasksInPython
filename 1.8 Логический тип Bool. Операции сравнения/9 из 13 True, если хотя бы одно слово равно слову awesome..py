'''
1.8 Логический тип Bool. Операции сравнения
9 из 13 шагов пройдено
18 из 33 баллов  получено
На вход поступают два слова.

Программа должна вывести True, если хотя бы одно слово равно слову "awesome".

Сделать задачу необходимо без использования условного оператора.

Sample Input 1:

cool
awesome
Sample Output 1:

True
Sample Input 2:

aaa
aaa
Sample Output 2:

False
'''
firstWord = str(input())
secondWord = str(input())
print(firstWord == 'awesome' or secondWord == 'awesome')
