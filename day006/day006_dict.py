if __name__ == '__main__':
    my_dict = {'Bruce': 190, 'Yoyo': 169}
    print(my_dict)
    print('my_dict[\'Bruce\'] --> %s' % my_dict['Bruce'])
    print('my_dict[\'Yoyo\'] --> %s' % my_dict['Yoyo'])
    print('To check whether key in dict: (\'Bruce\' in d) --> %s' % ('Bruce' in my_dict))
    print('my_dict.get(\'key\', default_value) --> d.get(\'Tom\', 170) --> %s' % (my_dict.get('Tom', 170)))
    if my_dict.get('key_not_exist') is None:
        print('my_dict.get(\'key_not_exist\') will get None --> %s' % (my_dict.get('key_not_exist')))
    print('my_dict.pop(\'key\') will delete key in dict --> %s' % my_dict)
    my_dict.pop('Bruce')
    print('my_dict.pop(\'key\') will delete key in dict --> %s' % my_dict)
