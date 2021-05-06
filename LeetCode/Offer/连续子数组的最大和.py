"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] +=nums[i - 1]
            max_number = max(max_number, nums[i])
        return max_number


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))