def count_letters(a):
    k_count = 0
    N_count = 0
    for i in a:
        if i.islower():
            k_count += 1
        if i.isupper():
            N_count += 1
    print(f'Количество заглавных символов: {N_count}')
    print(f'Количество строчных символов: {k_count}')


count_letters('QWERTY')
