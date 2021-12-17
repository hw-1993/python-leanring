if __name__ == '__main__':
    my_set = {1, 2, 3}
    print('Init set: my_set = {1, 2, 3} --> %s' % my_set)
    my_set.add(4)
    print('Using add() fn to add element to set: my_set.add(4) --> %s' % my_set)
    if 4 in my_set:
        my_set.remove(4)
    if 5 in my_set:
        # Check before remove, or you may get KeyError
        my_set.remove(5)
    print('Using remove() fn to remove element from set: my_set.remove(4) --> %s' % my_set)
    my_set_another = {2, 3, 4}
    print('my_set --> %s' % my_set)
    print('my_set_another --> %s' % my_set_another)
    print('my_set & my_set_another --> %s' % (my_set & my_set_another))
    print('my_set | my_set_another --> %s' % (my_set | my_set_another))
