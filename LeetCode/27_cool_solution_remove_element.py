class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

if __name__=="__main__":
    solution = Solution()
    solution.removeElement([0,1,2,2,3,0,4,2],2)