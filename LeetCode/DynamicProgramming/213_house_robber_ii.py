class Solution(object):
    def rob(self, nums): #mei xie chu lai
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def my_rob(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            memo = [0] * len(nums)
            memo[0] = nums[0]
            memo[1] = max(memo[0], nums[1])
            for i in range(2, len(nums)):
                memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
            return memo[len(nums) - 1]

        return max(my_rob(nums[1:]), my_rob(nums[:-1]))

    def rob_2variables(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def my_rob(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            prev1 = prev2 = 0
            for num in nums:
                temp = prev1
                prev1 = max(prev1, prev2 + num)
                prev2 = temp
            return prev1

        return max(my_rob(nums[1:]), my_rob(nums[:-1]))

if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1]))