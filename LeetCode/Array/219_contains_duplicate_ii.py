class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            else:
                dic[num] = i
        return False
if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    print(solution.containsNearbyDuplicate([99, 99], 2))