class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = len(nums) - 1
        while i >=0:
            if nums[i] == val:
                del nums[i]
            i -= 1
        return len(nums)

if __name__=="__main__":
    solution = Solution()
    solution.removeElement([0,1,2,2,3,0,4,2],2)
