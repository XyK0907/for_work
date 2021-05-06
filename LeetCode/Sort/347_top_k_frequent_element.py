import collections
import heapq
import itertools
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return list(zip(*sorted_dic))[0][:k]

    def topKFrequent_hashmap_heap(self, nums, k):
        """
        time nlogk if k < n
        :param nums:
        :param k:
        :return:
        """
        if k == len(nums):
            return nums
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


    def topKFrequent_bucketsort(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums).items()
        for num, freq in count:
            bucket[freq].append(num)
        return list(itertools.chain(*bucket))[-k:]

if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent_bucketsort(nums = [1,1,1,2,2,3], k = 2))
