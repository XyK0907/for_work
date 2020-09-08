def histogramm(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_hist(h):
    for c in sorted(h.keys()):
        print(c, h[c])


h = histogramm('parrot')
print_hist(h)