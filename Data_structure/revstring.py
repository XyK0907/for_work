from pythonds.basic import Stack

def revstring(mystr):
    s = Stack()
    for each in mystr:
        s.push(each)
    result = ''.join(s.pop() for i in range(s.size()))
    print(result)
    

revstring('apple')
