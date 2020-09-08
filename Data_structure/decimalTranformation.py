from pythonds.basic import Stack

def divideBy2(decNumber):
    """
    decimal to binary.
    :param decNumber:
    :return:
    """
    s = Stack()
    while decNumber > 0:
        s.push(decNumber % 2)
        decNumber = decNumber // 2

    return ''.join(str(s.pop()) for i in range(s.size()))

def baseConverter(decNumber,base):
    """
    decimal to binary.
    :param decNumber:
    :return:
    """
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    s = Stack()
    while decNumber > 0:
        s.push(decNumber % base)
        decNumber = decNumber // base

    return ''.join(digits[s.pop()] for i in range(s.size()))

print(divideBy2(233))
print(baseConverter(25,8))
print(baseConverter(26,26))