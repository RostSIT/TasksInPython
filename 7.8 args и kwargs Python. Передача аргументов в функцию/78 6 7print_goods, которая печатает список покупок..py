def print_goods(*args):
    b = {}
    couter = 0

    for i in args:
        if isinstance(i, str) and len(b) > 0:
            couter += 1
            b.setdefault(couter, i)
        else:
            print("Нет товаров")
            break
    for key, value in b.items():
        print(key, value)
    return ''


# def print_goods(*args, b=None):
#     if b is None:
#         b = []
#     for i in args:
#         if type(i) == str and len(i) != 0:
#             b.append(i)
#     if len(b) > 0:
#         for n in range(1, len(b) + 1):
#             print(f"{n}. {b[n - 1]}")
#     else:
#         print("Нет товаров")


print(print_goods('apple', 'banana', 'orange'))
