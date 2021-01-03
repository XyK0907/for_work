class Solution(object):
    def countBinarySubstrings(self, s): ##mei xie chu lai
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans

    def countBinarySubstrings1(self, s):
        import itertools
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))

    def countBinarySubstrings2(self, s):
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))

    def countBinarySubstrings_linear_scan(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)

    def countBinarySubstrings_rex(self, s):
        import re
        # groups = [len(list(v)) for _, v in groupby(s)]
        groups = list(map(len, re.findall('0+|1+', s)))
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBinarySubstrings_linear_scan('10011010011011'))

