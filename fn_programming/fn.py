def calc_sum(*args):
    ax = 0
    for num in args:
        ax = ax + num
    return ax


def lazy_sum(*args):
    def inner_sum():
        ax = 0
        for num in args:
            ax = ax + num
        return ax

    return inner_sum


def my_plus(x):
    return x * x


def is_odd(num):
    return num % 2 == 1


if __name__ == '__main__':
    print(calc_sum(1, 2, 3, 4, 5, 6))
    print(lazy_sum(1, 2, 3, 4, 5, 6))
    print(lazy_sum(1, 2, 3, 4, 5, 6)())
    fn0 = lazy_sum(1, 2, 3)
    fn1 = lazy_sum(1, 2, 3)
    print(fn0)
    print(fn1)
    print(fn0 == fn1)
    print(fn0())
    print(fn1())

    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(list(map(my_plus, my_list)))
    print(list(map(lambda x: x * x, my_list)))

    print(list(filter(is_odd, my_list)))
    print(list(filter(lambda n: n % 2 == 1, my_list)))
    print(list(filter(lambda n: n % 2 == 1, range(1, 50))))
