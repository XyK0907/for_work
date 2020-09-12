def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1


#in short
def firstUniqChar_1(self, s):
    return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])


def firstUniqChar_2(s):
    """
    :type s: str
    :rtype: int
    """
    ch=[]
    for i in set(s):
        if s.count(i) == 1:
            ch.append(s.index(i))
    if len(ch)>0:
        return min(ch)
    else:
        return -1

print(firstUniqChar('leetcode'))