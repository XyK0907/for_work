class Solution(object):
    def lengthOfLIS(self, nums): #mei xie chu lai
        """
        time O(n^2)
        space O(n)
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


    def lengthOfLIS_greedy_bs(self, nums): #kan bu dong
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(solution.lengthOfLIS([0,1,0,3,2,3]))
    print(solution.lengthOfLIS([7,7,7,7,7,7,7]))

