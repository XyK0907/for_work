class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        n = n - 2
        while n:
            c = a + b
            a = b
            b = c
            n -= 1
        return b

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))

