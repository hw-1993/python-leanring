class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_scope(self):
        print("%s: %s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'

    def get_scope(self):
        return self.__score

    def set_scope(self, scope):
        if 0 <= scope <= 100:
            self.__score = scope
        else:
            raise ValueError('bad scope')


if __name__ == '__main__':
    # 面向过程
    def print_scope(student):
        print("%s: %s" % (student['name'], student['scope']))


    s1 = {'name': 'Yoyo', 'scope': 100}
    s2 = {'name': 'Yoyo', 'scope': 100}
    print_scope(s1)
    print_scope(s2)

    # 面向对象
    yoyo = Student('Yoyo', 100)
    bruce = Student('Student', 80)
    peter = Student('Student', 59)
    yoyo.print_scope()
    bruce.print_scope()
    peter.print_scope()
    print(yoyo.get_grade())
    print(bruce.get_grade())
    print(peter.get_grade())
    print(peter.get_scope())
    peter.set_scope(100)
    print(peter.get_scope())
