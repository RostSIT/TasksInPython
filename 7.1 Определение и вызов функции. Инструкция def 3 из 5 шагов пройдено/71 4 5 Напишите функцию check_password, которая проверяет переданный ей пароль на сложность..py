def check_password(password):
    count_digit = 0
    count_upper = 0
    count_spec = 0
    for i in password:
        if i.isdigit():
            count_digit += 1

        if i.isupper():
            count_upper += 1

        if i in "!@#$%*":
            count_spec += 1

    if count_digit >= 3 and count_upper > 0 and count_spec > 0 and len(password) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")


check_password('Qwerty')
check_password('Qwerty1357!')

"""Сложным паролем будет считаться комбинация символов, в которой :

Есть хотя бы 3 цифры Есть хотя бы одна заглавная буква Есть хотя бы один символ из следующего набора "!@#$%*" Общая 
длина не менее 10 символов Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", 
в противном случае - "Easy peasy" 

Вам необходимо написать только определение функции

Разбор Youtube Patreon Boosty

Sample Input 1:

qwerty
Sample Output 1:

Easy peasy
Sample Input 2:

Qwerty1357!
Sample Output 2:

Perfect password"""
