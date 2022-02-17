def format_namelist(x):
    nameLIST = []
    finishList = []
    stoka = ''
    for i in range(len(x)):
        nameLIST.append(x[i]['name'])
    if len(nameLIST) == 0:
        return stoka
    elif len(nameLIST) == 1:
        for i in nameLIST:
            stoka = i
        return stoka
    else:
        for i in range(len(nameLIST)):
            if i == len(nameLIST):
                finishList.append(nameLIST[i])
            elif i == len(nameLIST) - 1:
                finishList.append('и')
                finishList.append(nameLIST[i])
            elif i == len(nameLIST) - 2:
                finishList.append(nameLIST[i])
            else:
                finishList.append(nameLIST[i] + ',')
    for i in finishList:
        stoka += i + ' '
    stoka = stoka[:-1]
    return stoka


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(format_namelist([{'name': 'Bart'}]))
print(format_namelist([]))


def format_namelist(dy):
    return ' и '.join(i['name'] for i in dy).replace(' и', ',', len(dy) - 2)


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(format_namelist([{'name': 'Bart'}]))
print(format_namelist([]))


def format_namelist(lst):
    a = []
    b = []
    c = []
    for i in range(len(lst)):
        a.append(lst[i]['name'])
    if len(a) > 1:
        a.append(a.pop(-2) + " и " + a.pop())
    return ', '.join(a)


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},  {'name': 'Maie'}]))
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(format_namelist([{'name': 'Bart'}]))
print(format_namelist([]))

"""7.3 Возвращаемое значение функции. Оператор return
6 из 8 шагов пройдено
9 из 18 баллов  получено
Ваша задача написать функцию format_namelist, которая принимает список словарей, у каждого словаря в списке есть только ключ name

Функция format_namelist должна вернуть отформатированную строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:

format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa и Maggie'

format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart и Lisa'

format_namelist([ {'name': 'Bart'} ])
# returns 'Bart'

format_namelist([])
# returns ''"""
