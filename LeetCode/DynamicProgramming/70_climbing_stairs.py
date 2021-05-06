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

    def climbStairs_math(self, n):
        """
        :type n: int
        :rtype: int
        """
        #fibonacci mathematically
        return int((5 ** .5 / 5) * (((1 + 5 ** .5) / 2) ** (n + 1) - ((1 - 5 ** .5) / 2) ** (n + 1)))

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))

