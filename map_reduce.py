from functools import reduce


def my_func(x):
    return x * x


def my_add(x, y):
    return x + y


def plus_ten_then_add(x, y):
    return x * 10 + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    def char2num_inner(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(char2num_inner, s))


if __name__ == '__main__':
    map_result = map(my_func, [1, 2, 3, 4, 5, 6])
    print(map_result)
    print(list(map_result))

    reduce_result = reduce(my_add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(reduce_result)
    print(reduce(plus_ten_then_add, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    int_result = reduce(plus_ten_then_add, map(char2num, '12345'))
    print(type(int_result))
    print(int_result)

    int_result_2 = str2int('12313123123123')
    print(type(int_result_2))
    print(int_result_2)
