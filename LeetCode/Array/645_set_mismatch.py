class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = [0] * len(nums)
        res = []
        for num in nums:
            if seen[num - 1] == 1:
                res.append(num)
            else:
                seen[num - 1] = 1
        res.append(seen.index(0) + 1)
        return res

    def findErrorNums_math(self, nums):
        n = len(nums)
        s = n * (n + 1) // 2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]



if __name__ == '__main__':
    solution = Solution()
    print(solution.findErrorNums([1,1]))