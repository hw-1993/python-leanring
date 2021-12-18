if __name__ == '__main__':
    sum_ = 0
    for x in range(10):
        sum_ = sum_ + x
    print(sum_)

    # define a list
    my_list = ['hello', 'world']
    for s in my_list:
        print(s)

    # define a immutable list
    my_immutable_list = ('e1', 'e2', 'e3')
    for s in my_immutable_list:
        print(s)

    if len(my_immutable_list) == 1:
        print(1)
    elif len(my_immutable_list) == 2:
        print(2)
    elif len(my_immutable_list) == 3:
        print(3)
    else:
        print('xxx')
