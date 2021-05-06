class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search_bisect(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))
    print(solution.search([-1,0,3,5,9,12], 2))