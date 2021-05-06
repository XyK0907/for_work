class Solution(object):
    def uniquePaths(self, m, n):
        """
        time O(mn)
        space O(mn0
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1
        d = [[0] * n for _ in range(m)]
        for i in range(m):
            d[i][0] = 1
        for j in range(n):
            d[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i - 1][j] + d[i][j - 1]
        return d[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3,3))