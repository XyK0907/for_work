class Solution(object):
    def moveZeroes(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1
        fast = slow + 1
        while fast < len(nums):
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], 0
                slow += 1
            fast += 1
        return nums

    def moveZeroes_precisetomine(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[tail],nums[i] = nums[i],nums[tail]
                tail += 1
        return nums

    def moveZeroes_snowball(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        snowballsize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowballsize += 1
            elif snowballsize > 0:
                nums[i - snowballsize], nums[i] = nums[i], 0
        return nums

if __name__ == '__main__':
    solution = Solution()
    # print(solution.moveZeroes([0,1,0,3,12, 0,0, 5]))
    print(solution.moveZeroes([1]))
    # solution.cool_moveZeroes([0,1,0,3,12, 0,0, 5])




