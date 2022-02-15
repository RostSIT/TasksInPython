
a = True
resolt = {'Били': set(), 'Вили': set(), 'Дили': set()}
while a == True:
    vvod = input()
    if vvod == 'конец':
        a = False
    else:
        name, value = vvod.split(': ')
        resolt[name].add(value)
for i in resolt:
    resolt[i] = len(resolt[i])
for i in sorted(resolt.items(), key=lambda para: -para[1]):
    print('Количество уникальных комментаторов у', i[0], '-', i[1])
