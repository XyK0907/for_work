class Solution(object):
    def rob(self, nums): # mei xie chu lai
        """
        main idea: rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        memo = [0, nums[0]]
        for i in range(1, len(nums)):
            val = nums[i]
            memo.append(max(memo[i - 1] + val, memo[i]))
        return memo[len(nums)]

    def rob_2variables(self, nums): # mei xie chu lai
        if not nums:
            return 0
        prev1 = prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1
