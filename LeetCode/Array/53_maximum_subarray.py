class Solution(object):
    def maxSubArray(self, nums):  # mei xie chu lai
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(1, len(nums)):
        #     if nums[i - 1] > 0:
        #         nums[i] += nums[i - 1]
        # return max(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray_oneliner(self, nums):  # mei xie chu lai
        """
        :type nums: List[int]
        :rtype: int
        """
        from itertools import accumulate
        return max(accumulate(nums, lambda x, y: x + y if x > 0 else y))