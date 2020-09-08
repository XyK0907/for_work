def check_fermat(a, b, c, n):
    if a ** n + b ** n == c **n:
        print('天哪，费马弄错了')
    else:
        print('不，那样不行')

if __name__ == '__main__':
    a = input('input a\n')
    b = input('input b \n')
    c = input('input c\n')
    n = input('input n\n')
    check_fermat(int(a), int(b), int(c), int(n))