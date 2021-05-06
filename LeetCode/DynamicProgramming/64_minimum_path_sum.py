class Solution(object):
    def minPathSum(self, grid):
        """
        time O(mn)
        space O(mn)
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        colomns = len(grid[0])
        d = [[0] * colomns] * rows
        for i in range(rows):
            for j in range(colomns):
                if i == 0 and j == 0:
                    d[i][j] = grid[i][j]
                elif i == 0:
                    d[i][j] = grid[i][j] + d[i][j - 1]
                elif j == 0:
                    d[i][j] = grid[i][j] + d[i - 1][j]
                else:
                    d[i][j] = min(grid[i][j] + d[i][j - 1], grid[i][j] + d[i - 1][j])
        return d[rows - 1][colomns -1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
    print(solution.minPathSum(grid = [[1,2,3],[4,5,6]]))

