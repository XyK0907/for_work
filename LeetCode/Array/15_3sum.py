class Solution(object):
    def threeSum(self, nums):
        """
        mei xie chu lai
        two pointer
        time O(n^2)
        space O(logn)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i >0 and nums[i] == nums[i -1]:
                continue
            k = length - 1
            target = -nums[i]
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res




if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))
