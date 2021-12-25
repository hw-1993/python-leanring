from functools import reduce


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(int_list):
    def multiply(x, y):
        return x * y

    return reduce(multiply, int_list)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(str_float):
    def char2num_inner(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    str0 = str_float.split(".")[0]
    str1 = str_float.split(".")[1]
    return reduce(fn, map(char2num_inner, str0)) + reduce(fn, map(char2num_inner, str1)) / (10 ** len(str1))


if __name__ == '__main__':
    list0 = ['bRuce', 'LISA', 'yoYo']
    list1 = list(map(normalize, list0))
    print(list0)
    print(list1)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
