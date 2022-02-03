"""5.5 Вложенные циклы 3 из 8 шагов пройдено 7 из 35 баллов  получено Постулат Бертрана Постулат Бертрана (теорема
Бертрана-Чебышева, теорема Чебышева) гласит, что для любого n > 1 найдется простое число p в интервале n < p < 2n.
Такая гипотеза была выдвинута в 1845 году французским математиком Джозефем Бертраном (проверившим ее до n=3000000) и
доказана в 1850 году Пафнутием Чебышевым. Рамануджан в 1920 году нашел более простое доказательство, а Эрдеш в 1932 –
еще более простое.

Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n найти количество простых
чисел p из интервала n < p < 2n.

Напомним, что число называется простым, если оно делится только само на себя и на единицу.

Входные данные
Программа принимает на вход целое число n (2 ≤ n ≤ 50000).

Выходные данные
Вам необходимо вывести на экран одно число – количество простых чисел p на интервале  n < p < 2n.

Разбор Youtube Patreon Boosty

Sample Input 1:

2
Sample Output 1:

1
Sample Input 2:

4
Sample Output 2:

2
"""

n = int(input())
count = 0
for p in range(n + 1, 2 * n):
    if p % 2 == 0 and p != 2 or p == 1:
        continue

    d = 3
    is_plain = True
    while d * d <= p:
        if p % d == 0:
            is_plain = False
            break
        d += 2
    if is_plain:
        count += 1

print(count)

