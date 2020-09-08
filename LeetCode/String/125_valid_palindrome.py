class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''.join(ch for ch in s if ch.isalnum()).lower()
        for i in range((len(new_s) + 1) // 2):
            if new_s[i] != new_s[len(new_s) -1 - i]:
                return False
        return True


if __name__=="__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))