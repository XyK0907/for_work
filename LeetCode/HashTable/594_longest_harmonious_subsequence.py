class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        dic = Counter(nums)
        # count = {}
        # for x in A:
        #     count[x] = count.get(x, 0) + 1

        res = 0
        for key in dic:
            if dic.get(key + 1):
                res = max(res, dic[key] + dic[key + 1])
        return res
