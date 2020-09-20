class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] == 0:
                zero_start = True
                j = i + 1
                while j < len(s) and s[j] == 0:
                    j += 1
