def apply_and_add(x, y, fn):
    return fn(x) + fn(y)


if __name__ == '__main__':
    print([1 / i for i in range(1, 10, 2)])
    print("sum = {:.6f}".format(sum([1 / i for i in range(1, 10, 2)])))
    print(apply_and_add(-10, -100, abs))
