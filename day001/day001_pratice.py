if __name__ == '__main__':
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f 华氏度 = %.1f 摄氏度' % (f, c))

    radius = float(input('请输入圆的半径：'))
    area = 3.1416 * (radius ** 2)
    perimeter = 2 * 3.1416 * radius
    print('圆的周长是 %.2f' % perimeter)
    print('圆的面积是 %.2f' % area)

    year = int(input('请输入年份：'))
    is_leap = year % 4 == 0 and year % 100 != 0 \
              or year % 400 == 0
    print('%d %s leap.' % (year, 'is' if is_leap else 'is not'))
