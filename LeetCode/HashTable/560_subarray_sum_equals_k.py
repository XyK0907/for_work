class Solution(object):
    def subarraySum(self, nums, k): #mei zuo chu lai
        """
        time O(n)
        space O(n)
        前缀和 + 哈希表优化
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        sum, res = 0, 0
        for each in nums:
            sum += each
            if (sum - k) in dic:
                res += dic[sum - k]
            dic[sum] = dic.get(sum, 0) + 1
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum(nums = [1,1,1], k = 2))
    print(solution.subarraySum(nums = [1,2,3], k = 3))