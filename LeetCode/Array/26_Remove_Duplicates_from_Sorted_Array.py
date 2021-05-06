class Solution(object):
    def removeDuplicates_two_pointer(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        apointer = 0
        bpointer = 1
        while bpointer < len(nums):
            if nums[bpointer] > nums[apointer]:
                apointer += 1
                nums[apointer] = nums[bpointer]
            bpointer += 1
        return apointer + 1



    def removeDuplicates_cool_solution(self, nums):
        """
        two pointer
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
    print(solution.removeDuplicates_two_pointer([1,1,1, 2,2, 3,3]))