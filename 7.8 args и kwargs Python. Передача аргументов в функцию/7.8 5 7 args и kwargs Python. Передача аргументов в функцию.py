def count_args(*args):
    count = 0
    for i in args:
        count += 1
    return count


print(count_args(1, 2, 4))


def count_args(*args):
    return len(args)


print(count_args(1, 2, 4))

