from pythonds.basic import Stack


def parChecker(symbolString):
    s = Stack()
    balance = True
    for each in symbolString:
        if each == '(':
            s.push(each)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
    if s.isEmpty() and balance:
        return True
    else:
        return False

def parChecker_general(symbolString):
    s = Stack()
    balance = True
    for each in symbolString:
        if each in '([{':
            s.push(each)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, each):
                    balance = False
    if s.isEmpty() and balance:
        return True
    else:
        return False


def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

print(parChecker('((()))'))
print(parChecker('(()((())()))'))
print(parChecker_general('{({([][])}())}'))
print(parChecker_general('[{()]'))