class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for each in nums:
            if each == 0:
                nums.remove(each)
                nums.append(0)
        print(nums)

    def cool_moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[tail],nums[i] = nums[i],nums[tail]
                tail += 1


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes([0,1,0,3,12, 0,0, 5])
    solution.cool_moveZeroes([0,1,0,3,12, 0,0, 5])




