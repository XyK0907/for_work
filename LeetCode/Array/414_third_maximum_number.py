class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i -1]:
                count += 1
            if count == 2:
                return nums[i]
        return nums[0]

    def thirdMax1(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        v = [float('-inf'),float('-inf'),float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
            return max(nums) if float('-inf') in v else v[2]

if __name__ == '__main__':
    solution = Solution()
    print(solution.thirdMax(nums = [3,2,1]))
    print(solution.thirdMax([1, 2]))
    print(solution.thirdMax([2, 2, 3, 1]))