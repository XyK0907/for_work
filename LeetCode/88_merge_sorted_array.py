class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        return nums1

if __name__ == "__main__":  
    solution = Solution()
    print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))