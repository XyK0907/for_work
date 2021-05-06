class Solution(object):
    def countNegatives(self, grid):
        """
        Time: O(mlogn)
        Space: O(n)
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            l, r = 0, len(grid[i]) - 1
            while l <=r:
                mid = l + (r - l) // 2
                if grid[i][mid] >= 0:
                    l = mid + 1
                else:
                    r = mid -1
            count += len(grid[i][l:])
        return count

    def countNegatives_1(self, grid):
        """
        Time: O(m + n)
        :type grid: List[List[int]]
        :rtype: int
        """
        i = len(grid)-1
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            print(i,j)
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)


    def countNegatives_2(self, grid):
        """
        Time: O(n ^ 2)
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(a < 0 for r in grid for a in r)

        return (np.array(grid) < 0).sum()


if __name__ == "__main__":
    solution = Solution()
    print(solution.countNegatives_1([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(solution.countNegatives([[1,-1],[-1,-1]]))
    print(solution.countNegatives(grid = [[-1]]))