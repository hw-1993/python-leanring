def is_odd(num):
    return num % 2 == 1


def is_even(num):
    return num % 2 == 0


def not_empty(s):
    return s and s.strip()


if __name__ == '__main__':
    print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])))
    print(list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])))
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
