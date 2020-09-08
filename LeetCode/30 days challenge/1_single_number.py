class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in set(nums):
            if nums.count(item) == 1:
                return item


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2,2,1]))