def first_unique_char(string):
    uniqueSymbol = ""
    for i in string:
        if i not in uniqueSymbol and string.count(i) == 1:
            uniqueSymbol = string.index(i)
            break
    if uniqueSymbol == "":
        uniqueSymbol = -1
    return uniqueSymbol


print(first_unique_char('python'))
print(first_unique_char('abracadabra'))
print(first_unique_char('abcabc'))


def first_unique_char(array):
    for i, num in enumerate(array):
        if array.count(num) == 1:
            return i
    return -1


print(first_unique_char('python'))
print(first_unique_char('abracadabra'))
print(first_unique_char('abcabc'))

def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1

print(first_unique_char('python'))
print(first_unique_char('abracadabra'))
print(first_unique_char('abcabc'))

print(enumerate(array))

"""7.3 Возвращаемое значение функции. Оператор return
5 из 8 шагов пройдено
4 из 18 баллов  получено
Напишите функцию first_unique_char, которая принимает строку символов и возвращает позицию первого уникального символа в строке. В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.

Ваша задача написать только определение функции first_unique_char

Sample Input 1:

python
Sample Output 1:

0
Sample Input 2:

abracadabra
Sample Output 2:

4
Sample Input 3:

abcabc
Sample Output 3:

-1"""