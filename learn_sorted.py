# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


if __name__ == '__main__':
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=by_name))
    print(sorted(L, key=by_score, reverse=True))
