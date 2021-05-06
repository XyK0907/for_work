class Solution(object):
    def containsDuplicate(self, nums):
        """
        or seen method in hash map
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        if not nums:
            return False
        dic = Counter(nums)
        return not max(dic.values()) == 1

    def containsDuplicate_sorting(self, nums):
        """
        time O(nlogn)
        space O(1)
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i -1]:
                return True
        return False

    def containsDuplicate_easy(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 4]))