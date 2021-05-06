class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n
        while n > 0:
            if m < 1:
                m = 1
                nums1[m -1: n] = nums2[:n]
                break
            else:
                if nums2[n - 1] > nums1[m - 1]:
                    nums1[tail - 1] = nums2[n - 1]
                    tail -= 1
                    n -= 1
                else:
                    nums1[tail -1] = nums1[m -1]
                    tail -= 1
                    m -= 1
        print(nums1)




if __name__ == "__main__":  
    solution = Solution()
    # print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
    # print(solution.merge([0], 0, [1], 1))
    # print(solution.merge([2,0,0], 1, [1, 3], 2))
    print(solution.merge([4, 5, 6, 0, 0, 0], 3, [1,2,3], 3))
