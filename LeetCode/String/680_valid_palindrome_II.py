class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        situation_1 = False
        situation_2 = False
        for i in range((len(s) + 1) // 2):
            if s[i] != s[len(s) - 1 - i]:
                if s[i] == s[len(s) -2 -i]:
                    new_s = s[i: len(s) - 1 - i]
                    situation_1 = new_s == new_s[::-1]
                if s[i + 1] == s[len(s) -1 - i]:
                    new_s = s[i + 1: len(s) - i]
                    situation_2 = new_s == new_s[::-1]
                return situation_1 or situation_2
        return True


if __name__=="__main__":
    solution = Solution()
    print(solution.validPalindrome("cbbcc"))