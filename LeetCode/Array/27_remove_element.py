class Solution(object):
    def removeElement(self, nums, val):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        tail = -1
        for i in range(len(nums)):
            if nums[i] != val:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1

    def removeElement_rarenum(self, nums, val):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

if __name__=="__main__":
    solution = Solution()
    print(solution.removeElement([1,1,1, 2,2, 3,3], 2))
