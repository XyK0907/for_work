from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

    def longestPalindrome1(self, s):
        odds = sum([freq % 2 for _, freq in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1

    def longestPalindrome2(self, s):
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)  # 如果有奇数，总能将其放到中间