


class Solution(object):
    def findTargetSumWays(self, nums, S): #TLE
        """
        time O(2^n)
        space O(n)
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        self.calculate(nums, 0, 0, S)
        return self.count

    def calculate(self, nums, i, s, S):
        if i == len(nums):
            if s == S:
                self.count += 1
        else:
            self.calculate(nums, i + 1, s + nums[i], S)
            self.calculate(nums, i + 1, s - nums[i], S)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))

