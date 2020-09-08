def histogramm(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_lookup(d,v):
    a = []
    for k in d:
        if d[k] == v:
            a.append(k)
    return a


h = histogramm('parrot')
print(reverse_lookup(h, 3))