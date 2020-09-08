class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #fibonacci mathematically
        return int((5 ** .5 / 5) * (((1 + 5 ** .5) / 2) ** (n + 1) - ((1 - 5 ** .5) / 2) ** (n + 1)))

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(6))
