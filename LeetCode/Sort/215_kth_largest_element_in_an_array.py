import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        time nlogn
        space n
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        dic = {}
        for each in nums:
            dic[each] = dic.get(each, 0) + 1
        for key, v in sorted(dic.items(), reverse=True):
            count += v
            if count >= k:
                return key


    def findKthLargest_easist(self, nums, k):
        """
        time nlogn
        space 1
        :param nums:
        :param k:
        :return:
        """
        return sorted(nums)[-k]

    def findKthLargest_selectionsort(self, nums, k):
        """
        time nk
        space 1
        :param nums:
        :param k:
        :return:
        """
        for i in range(len(nums) - 1):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            if i != minIndex:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums[len(nums) - k]

    def findKthLargest_minheap(self, nums, k):
        """
        time nlogn
        space n
        :param nums:
        :param k:
        :return:
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    def findKthLargest_minheap1(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heap[0]

    def findKthLargest_minheap2(self, nums, k):
        return heapq.nlargest(k,nums)[-1]

    def findKthLargest_quickselection(self, nums, k):
        """
        time n^2
        :param nums:
        :param k:
        :return:
        """
        if not nums: return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest_quickselection(left, k)
        if k > L + M:
            return self.findKthLargest_quickselection(right, k - L - M)
        else:
            return mid[0]