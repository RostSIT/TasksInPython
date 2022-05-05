a = input()
b = input().split()
for i in b:
    if a in i:
        print(i)


"""Входные данные
На первой строке вводится один символ — строчная буква.
На второй строке вводится предложение.

Выходные данные
Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.

Sample Input 1:

a
Mary had a little lamb.
Sample Output 1:

Mary
had
a
lamb.
Sample Input 2:

e
Actions speak louder than words
Sample Output 2:

speak
louder"""