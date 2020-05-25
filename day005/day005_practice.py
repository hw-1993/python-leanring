import day005.module1 as m1
import day005.module2 as m2
import math


def fn1(n=2):
    print(n)


def fn2(*args):
    for arg in args:
        print(arg, end='')
    print()


if __name__ == '__main__':
    print(math.factorial(3))
    print(math.factorial(4))
    print(math.factorial(5))
    fn1()
    fn1(3)
    fn2('hello world')
    fn2(1, 2, 3, 45)
    m1.foo()
    m2.foo()
