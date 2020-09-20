class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.istitle() or word.isupper() or word.islower()


if __name__ == '__main__':
    solution = Solution()
    print(solution.detectCapitalUse('USA'))