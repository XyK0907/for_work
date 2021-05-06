class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Time: O(n + m)
        Space: O(n + m)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(set(nums1)) <= len(set(nums2)):
            return [each for each in set(nums1) if each in set(nums2)]
        return [each for each in set(nums2) if each in set(nums1)]

    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        from collections import Counter
        n1 = Counter(nums1)
        for each in nums2:
            if each in n1.keys() and each not in res:
                res.append(each)
        return res

    def intersection2(self, nums1, nums2):
        """
        Build-in set intersection
        Time complexity : O(n+m) in the average case and
        O(n×m) in the worst case when load factor is high enough.
        Space complexity : O(n+m)in the worst case when all elements in the arrays are different
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
    print(solution.intersection([4, 9, 5], [9,4,9,8,4]))