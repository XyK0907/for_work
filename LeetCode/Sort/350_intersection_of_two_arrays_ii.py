class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = {}
        ll = []
        from collections import Counter
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        for each in n1.keys():
            if each in n2.keys():
                res[each] = min(n1[each], n2[each])
        for key in res.keys():
            ll.extend([key] * res[key])
        return ll

    def intersect_solution1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())

    def intersect_solution2(self, nums1, nums2):
        """
        two pointers
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res

    def intersect_solution3(self, nums1, nums2):
        """
        two pointers
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num
                counts[num] -= 1

        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect_solution1([1, 2, 2, 1], [2, 2]))
    print(solution.intersect_solution1([4, 9, 5], [9,4,9,8,4]))
    print(solution.intersect_solution1([1, 1], [1, 1, 2]))