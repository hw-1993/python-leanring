def fn1():
    print('string * 3: %s' % ('fn1' * 3))
    print('\'hello\' + \'world\': %s' % ('hello' + 'world'))


def fn2():
    print('r\'\\nfn2\\n\': %sl' % r'\nfn2\n')
    print(r'\nfn2\n: %s' % '\nfn2\n')


def fn3():
    print('\'hello\' in \'hello world\': %s' % ('hello' in 'hello world'))
    print('\'python\' not in \'hello world\': %s' % ('python' not in 'hello world'))


def fn4():
    print('string[2:5]: %s' % 'string'[2:5])
    print('string[2:]: %s' % 'string'[2:])
    print('string[:5]: %s' % 'string'[:5])
    print('string[::2]: %s' % 'string'[::2])
    print('string[2::2]: %s' % 'string'[2::2])


def fn5():
    msg = 'hello world'
    print(len(msg))
    print('msg: %s' % msg)
    print('msg.capitalize(): %s' % msg.capitalize())
    print('msg.upper(): %s' % msg.upper())
    print('msg.lower(): %s' % msg.lower())
    print('msg.title(): %s' % msg.title())
    print('msg.center(50, \'*\'): %s' % msg.center(50, '*'))
    print('msg.rjust(50, \' \'): %s' % msg.rjust(50, ' '))
    print('msg.ljust(50, \' \'): %s' % msg.ljust(50, ' '))


def fn6():
    print('{0} {1} {2}'.format('a', 'b', 'c'))
    print('{0} {2} {1}'.format('a', 'b', 'c'))
    print('%s %s %s' % ('a', 'b', 'c'))


def main():
    str1 = 'hello world'
    str2 = """
    hello
    world"""
    str3 = '\'hello world\\ Java!\\n'
    print(str1, str2, str3, sep='\n')
    fn1()
    fn2()
    fn3()
    fn4()
    fn5()
    fn6()


if __name__ == '__main__':
    main()
