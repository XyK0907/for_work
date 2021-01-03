class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        i = len(nums)-1
        while i>=0:
            if nums[i] == nums[i-1]:
                del nums[i]
                if len(nums) == 1:
                    return 1
            i -=1
        return len(nums)

    def removeDuplicates_cool_solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

if __name__=="__main__":
    solution = Solution()
    solution.removeDuplicates([1,1,1])