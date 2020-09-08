import math
def square_root(a):
    x = 3
    while True:
        y = (x + a/x) / 2
        if abs(x - y) < 0.0000001:
            break
        x = y
    return y


if __name__ == '__main__':
    for i in range(9):
        first = square_root(i)
        second = math.sqrt(i)
        print(i , '\t' , first, '\t', second, '\t', abs(first - second))