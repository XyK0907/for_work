class Solution(object):
    def wiggleMaxLength_greedy(self, nums): #mei xie chu lai
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        prevdiff = nums[1] - nums[0]
        count = 2 if prevdiff else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i -1]
            if (prevdiff <= 0 and diff > 0) or (prevdiff >= 0 and diff < 0):
                count += 1
                prevdiff = diff
        return count

    def wiggleMaxLength_dp(self, nums):
        """
        time O(n^2)
        space O(n)
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return len(nums)
        up = [0] * len(nums)
        down = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        return 1 + max(up[len(nums) - 1], down[len(nums) - 1])

    def wiggleMaxLength_lineardp(self, nums):
        """
        time O（n）
        space O(n)
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return len(nums)
        up = [1] * len(nums)
        down = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(down[len(nums) - 1], up[len(nums) - 1])

    def wiggleMaxLength_lineardp_optimized(self, nums):
        """
        time O(n)
        space O(1)
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return len(nums)
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(down, up)

if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))