class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        reversed_number = int(str(x)[::-1])
        if reversed_number == x:
            return True
        else:
            return False

if __name__=="__main__":
    solution = Solution()
    solution.isPalindrome(-121)