class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        if nums:
            self.cache = {0: nums[0]}
            for i in range(1, len(nums)):
                self.cache[i] = nums[i] + self.cache[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        if i == 0:
            return self.cache[j]
        else:
            return self.cache[j] - self.cache[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)