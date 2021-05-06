class Solution(object):

    def strStr(self, haystack, needle):
        """
        time O((n - l) L)
        space O(1)
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr_two_pointers(self, haystack, needle):
        """
        time O((n - l) L)
        space O(1)
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, L = len(haystack), len(needle)
        if L == 0:
            return 0
        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
            pl = 0
            count = 0
            while pl < L and pn < n and haystack[pn] == needle[pl]:
                count += 1
                pn += 1
                pl += 1
            if count == L:
                return pn - L
            pn = pn - count + 1
        return -1


if __name__=="__main__":
    solution = Solution()
    print(solution.strStr("mississippi","pip"))
