'''
1.8 Логический тип Bool. Операции сравнения
8 из 13 шагов пройдено
15 из 33 баллов  получено
На вход поступает целое число.

Программа должна вывести True, если введенное значение принадлежит интервалу от 5 не включительно до 19 включительно , в противном случае - False.

Сделать задачу необходимо без использования условного оператора.

Sample Input 1:

10
Sample Output 1:

True
Sample Input 2:

5
Sample Output 2:

False
Sample Input 3:

19
Sample Output 3:

True
'''

var = int(input())
print(5 < var <= 19)