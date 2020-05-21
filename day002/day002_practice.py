def cal_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'


if __name__ == '__main__':
    username = str(input('Please input your username: '))
    password = str(input('Please input your password: '))
    if username == 'admin' and password == '12345':
        print('Welcome!')
    else:
        print('Incorrect username and password')

    x = float(input('Please number x: '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))

    scope = float(input('Please input your scope, so you can get your grade.'))
    print(cal_grade(scope))
