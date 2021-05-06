class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        i, j = 0, 0
        while i <= len(s) - 1 and j <= len(t) - 1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

    def isSubsequence_iter(self, s, t):
        """
        Time: O(s + t)
        Space:O(1)
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)
        return all(c in t for c in s)

    def isSubsequence_iter2style(self, s, t):
        """
        for c in s:
            i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
        return True

        :type s: str
        :type t: str
        :rtype: bool
        """
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

    def isSubsequence_binarysearch(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        from bisect import bisect_left
        def createMap(s):
            # create a map. key is char. value is index of apperance in acending order.
            posMap = defaultdict(list)
            for i, char in enumerate(s):
                posMap[char].append(i)
            return posMap

        posMap = createMap(t)
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True

    def isSubsequence_dp(self, s, t):
        from itertools import product
        s, t = "!" + s, "!" + t
        m, n = len(s), len(t)
        dp = [[0] * m for _ in range(n)]
        for i in range(n): dp[i][0] = 1

        for i, j in product(range(1, n), range(1, m)):
            if s[j] == t[i]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence_binarysearch('abcd', 'ahbgdc'))
    # print(solution.isSubsequence('axc', 'ahbgdc'))
    # print(solution.isSubsequence('', 'ahbgdc'))
    print(solution.isSubsequence('leeeeetcode', "ylyeyeyeyeyeyeytycyoydyey"))