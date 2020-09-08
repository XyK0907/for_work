class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))