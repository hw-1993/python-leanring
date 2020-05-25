from random import randint


def is_narcissistic_number(x):
    """
    判断数字是否为水仙花数。水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数
    它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
    例如：$1^3 + 5^3+ 3^3=153$。
    :param x:
    :return:
    """
    number_str = str(x)
    if len(number_str) != 3:
        return False
    number_int = int(x)
    high = number_int // 100
    middle = number_int // 10 % 10
    low = number_int % 10
    if low ** 3 + middle ** 3 + high ** 3 == number_int:
        return True
    return False


def reverse_number(x):
    """
    反转数字
    :param x:
    :return:
    """
    num = int(x)
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


def fn1():
    """
    百钱百鸡问题: 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡
    问公鸡、母鸡、小鸡各有多少只？
    :return:
    """
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


def craps_game():
    """
    CRAPS又称花旗骰
    简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
    其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
    其他点数，玩家继续要骰子，直到分出胜负。
    :return:
    """
    money = int(input('请下注：'))
    first = randint(1, 6) + randint(1, 6)
    needs_go_on = False
    print('first round!')
    print('你的点数 %d' % first)
    if first == 7 or first == 11:
        print('you win %d' % money)
    elif first == 2 or first == 3 or first == 12:
        print('you lose %d' % money)
    else:
        needs_go_on = True
    while needs_go_on:
        print('another round!')
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('你的点数 %d' % current)
        if current == first:
            print('you win %d' % money)
        elif current == 7:
            print('you lose %d' % money)
        else:
            needs_go_on = True


def is_prefect_number(x):
    sum_x = 0
    for i in range(1, x):
        y = x % i
        if y == 0:
            sum_x += i
    return sum_x == x


def print_prefect_number():
    for x in range(10000):
        print('', end='')
        if is_prefect_number(x):
            print(x, end=', ')
    print()


if __name__ == '__main__':
    reverse_number(12345)
    fn1()
    print_prefect_number()
    craps_game()
    number = int(input('Please input number: '))
    print('%d %s水仙花数' % (number, '是' if is_narcissistic_number(number) else '不是'))
