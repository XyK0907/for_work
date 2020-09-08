import math

def eval_loop():
    result = 0
    while True:
        a = input('输入一个字符串\n')
        if a == 'done':
            break
        else:
            result = eval(a)
            print(result)
    return result


if __name__ == '__main__':
    eval_loop()