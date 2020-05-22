a = 321
b = 123
c = 12.345
d = 'hello world'
e = True
f = False

if __name__ == '__main__':
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

    # use builtin fn type() to type check
    print(type(a))
    print(type(c))
    print(type(d))
    print(type(e))

    # builtin type convert fn
    num_str = '1234'
    print(type(int(num_str)))
    print(type(str(1234)))
    print(chr(97))
    print(ord('a'))

    # use builtin fn input() to get input from keyboard
    num1 = int(input('please input number a: '))
    num2 = int(input('please input number b: '))
    print('%d + %d = %d' % (num1, num2, num1 + num2))
    print('%d - %d = %d' % (num1, num2, num1 - num2))
    print('%d * %d = %d' % (num1, num2, num1 * num2))
    print('%d / %d = %d' % (num1, num2, num1 / num2))
    print('%d %% %d = %d' % (num1, num2, num1 % num2))
