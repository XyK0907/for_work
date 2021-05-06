class Solution(object):
    def canPartition(self, nums):
        """
        背包问题
        time O(n * target)
        space O(n * target)
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        sumNum = sum(nums)
        maxNum = max(nums)
        if sumNum % 2 == 1:
            return False
        else:
            target = sumNum // 2
        if maxNum > target:
            return False

        rows = len(nums)
        dp = [[False] * (target + 1) for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, rows):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[rows - 1][target]


    def canPartition_space_opt(self, nums):
        """
        背包问题
        time O(n * target)
        space O(target)
        :type nums: List[int]
        :rtype: bool
        """
        rows = len(nums)
        if rows < 2:
            return False
        sumNum = sum(nums)
        if sumNum % 2 == 1:
            return False
        else:
            target = sumNum // 2

        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]
