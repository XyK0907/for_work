class Solution(object):
    def searchInsert(self, nums, target):
        """
        Linear Search
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert_bisect(self, nums, target):
        """
        using bisect module
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)

    def searchInsert_binary_search(self, nums, target):
        """
        Binary Search by hand
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__=="__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6],4))
    print(solution.searchInsert_binary_search([1,3,5,6],4))