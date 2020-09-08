class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for i in range(len(grid)):
            if grid[i][0] == '1':
                for j in range(len(grid[i])):
                    if grid[0][j] == '1':
                        continue
                    else:
                        return i, j - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([["1","1","0","0","0"],
                               ["1","1","0","0","0"],
                               ["0","0","1","0","0"],
                               ["0","0","0","1","1"]]))
