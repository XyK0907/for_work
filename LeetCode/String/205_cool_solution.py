class Solution(object):
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)

    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):
        print([s.find(i) for i in s])
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic5(self, s, t):
        print(list(map(s.find, s)))
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True

    def isIsomorphic6(self, s, t):
        d1, d2 = dict(), dict()
        for v, w in zip(s, t):
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic5('add', 'egg'))