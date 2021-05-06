class Solution(object):
    def twoSum(self, nums, target):
        """
        time O(n^2)
        space O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == new_target:
                    return [i, j]


    def twoSum_hash(self, nums, target):
        """
        time O(n)
        space O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, value in enumerate(nums):
            new_target = target - value
            if new_target in dic:
                return [i, dic[new_target]]
            dic[value] = i
