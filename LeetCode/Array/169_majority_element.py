class Solution(object):
    def majorityElement(self, nums):
        """
        Hash Map
        Time O(n)
        Space O(n)
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        dic = Counter(nums)
        max_val = max(dic, key=dic.get)
        return max_val


    def majorityElement_sorting(self, nums):
        """
        Sorting
        Time O(nlogn)
        Space O(1) or O(n)
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]


    def majorityElement_boyermoore_voting(self, nums):
        """
        Boyer-Moore Voting algorithm
        Time O(n)
        Space O(1)
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))