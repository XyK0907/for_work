class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ori_row = len(nums)
        ori_col = len(nums[0])
        if r * c != ori_row * ori_col or not nums or not nums[0]:
            return nums
        ans = []
        row = []
        for i in range(ori_row):
            for j in range(ori_col):
                if len(row) != c:
                    row.append(nums[i][j])
                else:
                    ans.append(row)
                    row = [nums[i][j]]
        ans.append(row)
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixReshape(nums = [[1,2],[3,4]], r = 2, c = 4))
