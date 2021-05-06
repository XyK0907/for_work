class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * (len(nums)+ 1)
        for each in nums:
            res[each] = each
        if 0 in res[1:]:
            return res.index(0, 1)
        else:
            return 0

    def missingNumber_gauss(self, nums):
        """
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        expected_sum = length * (length + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missingNumber_sorting(self, nums):
        """
        time O(nlogn)
        space O(1) or O(n)
        :param nums:
        :return:
        """
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


    def missingNumber_hash(self, nums):
        """
        hashset
        time O(n)
        space O(n)
        :param nums:
        :return:
        """
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


    def missingNumber_bit(self, nums):
        """
        bit manipulation
        time O(n)
        space O(1)
        :param nums:
        :return:
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber_gauss([3,0,1]))
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))