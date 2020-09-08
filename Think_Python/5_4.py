def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('No')
    elif a + b == c or a + c == b or b + c == a:
        print('退化三角形')
    else:
        print('Yes')


if __name__ == '__main__':
    a = input('input a\n')
    b = input('input b \n')
    c = input('input c\n')
    is_triangle(int(a), int(b), int(c))