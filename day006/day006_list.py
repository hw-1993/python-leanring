def fn_list_example():
    list1 = [1, 'hello', 'world', 4, 5]
    list2 = ['message'] * 3
    print(list1)
    print(list2)
    print(len(list2))
    print(list2[0], list2[1], list2[2])
    for ele in list1:
        print(ele, end=' - ')
    print()
    for index, ele in enumerate(list2):
        print(index, ele)


def fn_list_operation():
    list3 = ['list']
    list3.append('append')
    list3.insert(0, 'insert')
    print(list3)
    list3.reverse()
    print(list3)
    list3.clear()
    print(list3)


def fn():
    list4 = [x for x in range(1, 10)]
    list5 = [x + y for x in 'ABCDEFGH' for y in '1234566']
    print(list4)
    print(list5)


def main():
    fn_list_example()
    fn_list_operation()
    fn()


if __name__ == '__main__':
    main()
