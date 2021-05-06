class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive = False
        start = 0
        maxnumber = 0
        for i in range(len(nums)):
            if nums[i] == 1 and not consecutive:
                start = i
                consecutive = True
            elif nums[i] == 1 and consecutive:
                continue
            elif nums[i] != 1 and consecutive:
                consecutive = False
                maxnumber = max(maxnumber, i - start)

        if consecutive:
            maxnumber = max(maxnumber, len(nums) - start)

        return maxnumber

    def findMaxConsecutiveOnes_eash(self, nums):
        """
        time O(n)
        space O(1)
        :param nums:
        :return:
        """
        count = maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        maxCount = max(maxCount, count)
        return maxCount

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(solution.findMaxConsecutiveOnes([1,0,0, 1,1]))

