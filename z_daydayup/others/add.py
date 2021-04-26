def add(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
    else:
        return '请输入正确算法！'


add(1, 2, '+')
print(add(1, 2, '-'))

