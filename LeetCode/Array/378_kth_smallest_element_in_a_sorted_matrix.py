class Solution(object):
    def kthSmallest(self, matrix, k): #mei xie chu lai
        """
        time O(nlog(r -l))
        space O(1)
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] > mid:
                    i -= 1
                else:
                    num += i + 1
                    j += 1
            return num >= k

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
