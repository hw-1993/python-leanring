# Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，
# 前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些标识符，
# 我们之前用过的input、print、int等都属于内置作用域
def foo():
    # b 为函数局部变量，属于局部作用域
    # b 对于 bar 而言，属于嵌套作用域
    b = 'hello'
    global fuxx
    fuxx = 'fuck in foo'
    print(fuxx)

    # Python中可以在函数内部再定义函数
    def bar():
        # c 为函数局部变量，属于局部作用域
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    # a 为全局变量，属于全局作用域
    a = 100
    fuxx = 'fuck'
    print(fuxx)
    # print(b)  # NameError: name 'b' is not defined
    foo()
    print(fuxx)
