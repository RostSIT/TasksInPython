# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name, age):
#     if age >= MIN_DRIVING_AGE:
#         print(f'{name} может водить')
#     else:
#         print(f'{name} еще рано садиться за руль')

MIN_DRIVING_AGE = 18
ANSWERS = ("еще рано садиться за руль", "может водить")


def allowed_driving(name, age):
    print(f'{name} {ANSWERS[age >= MIN_DRIVING_AGE]}')


print(allowed_driving('tim', 17))
print(allowed_driving('bob', 18))

"""7.6 Область видимости: локальная, глобальная и встроенная. 2 из 2 шагов пройдено 1 из 1 баллa  получен Напишите
функцию, которая имя и возраст водителя. Функция должна распечатать на экран заключение, может ли данный водитель 
управлять транспортом и определять она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE 

Если водитель может управлять, выведите фразу "<name> может водить> " , в противном случае "<name> еще рано садиться 
за руль" 

MIN_DRIVING_AGE = 18
allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
allowed_driving('bob', 18) # выведет "bob может водить"""
