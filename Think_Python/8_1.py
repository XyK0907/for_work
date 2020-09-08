def backwards(s):
    n = len(s)
    while n > 0:
        print(s[n-1])
        n -= 1

backwards('abcdefg')