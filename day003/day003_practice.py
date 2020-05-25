import random


def sum100():
    number = 0
    # range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
    # range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
    # range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
    # range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
    for x in range(101):
        number += x
    print(number)


def sum_old(num):
    number = 0
    for i in range(int(num)):
        if i % 2 == 0:
            number += i
    print(number)


def guess_number_game():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('您的猜测 (1~100): '))
        if number < answer:
            print('您的猜测偏小')
        elif number > answer:
            print('您的猜测偏大')
        else:
            print('您猜对了')
            break
    print('您总共猜了 %d 次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d' % (j, i, i * j), end='\t')
        print()


def is_prime_number(num):
    """
    素数指的是只能被1和自身整除的正整数（不包括1）。
    :param num:
    :return:
    """
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    return is_prime and num > 1


def prime_number():
    print('%d %s prime number' % (2, 'is' if is_prime_number(2) else 'is not'))
    print('%d %s prime number' % (3, 'is' if is_prime_number(3) else 'is not'))
    print('%d %s prime number' % (5, 'is' if is_prime_number(5) else 'is not'))
    print('%d %s prime number' % (7, 'is' if is_prime_number(7) else 'is not'))
    print('%d %s prime number' % (11, 'is' if is_prime_number(11) else 'is not'))
    print('%d %s prime number' % (12, 'is' if is_prime_number(12) else 'is not'))
    print('%d %s prime number' % (13, 'is' if is_prime_number(13) else 'is not'))


def triangle_display(line):
    for i in range(1, line + 1):
        for j in range(1, i + 1):
            print('*', end='')
        print()

    for i in range(line):
        for j in range(line):
            if j < line - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(line):
        for j in range(line - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()


def calc_gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor_ in range(x, 0, -1):
        if x % factor_ == 0 and y % factor_ == 0:
            return factor_


def calc_lcm(x, y):
    return x * y // calc_gcd(x, y)


if __name__ == '__main__':
    sum100()
    sum_old(200)
    sum_old(6)
    multiplication_table()
    prime_number()
    triangle_display(5)

    # 两个数的最大公约数是两个数的公共因子中最大的那个数
    # 两个数的最小公倍数则是能够同时被两个数整除的最小的那个数
    # 两个数的乘积等于这两个数的最大公约数与最小公倍数的乘积
    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))
    if num1 < num2:
        num1, num2 = num2, num1
    for factor in range(num2, 0, -1):
        if num1 % factor == 0 and num2 % factor == 0:
            print('%d 和 %d 的最大公约数为 %d' % (num1, num2, factor))
            print('%d 和 %d 的最小公倍数为 %d' % (num1, num2, num1 * num2 // factor))
            break

    print('%d 和 %d 的最大公约数为 %d' % (num1, num2, calc_gcd(num1, num2)))
    print('%d 和 %d 的最小公倍数为 %d' % (num1, num2, calc_lcm(num1, num2)))

    guess_number_game()
