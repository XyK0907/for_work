class Solution(object):
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)

if __name__=="__main__":
    solution = Solution()
    solution.isPalindrome(12321)