class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        odd =False
        longest = 0

        for each, num in Counter(s).items():
            if num % 2 == 1:
                odd = True
                longest += num - 1
            else:
                longest += num

        if odd:
            return longest + 1
        else:
            return longest



if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez'))