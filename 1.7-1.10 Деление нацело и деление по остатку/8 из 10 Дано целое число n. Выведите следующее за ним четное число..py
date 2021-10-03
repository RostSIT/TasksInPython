'''
1.7 Деление нацело и деление по остатку
8 из 10 шагов пройдено
13 из 20 баллов  получено
Следующее четное

Дано целое число n. Выведите следующее за ним четное число.

Задачу необходимо решить целочисленными операциями без
использования условных операторов и\или циклов.

Sample Input 1:

5
Sample Output 1:

6
Sample Input 2:

6
Sample Output 2:

8
'''
def findTheNextEvenNumber():

    someNumber = int(input())
    nextEvenNumber = someNumber - someNumber % 2 + 2
    print(nextEvenNumber)

findTheNextEvenNumber()

# def findTheNextEvenNumber(someNumber):
#
#     nextEvenNumber = someNumber - someNumber % 2 + 2
#     print(nextEvenNumber)
#
# findTheNextEvenNumber(5)
