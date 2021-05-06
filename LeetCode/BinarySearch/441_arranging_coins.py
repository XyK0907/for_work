class Solution(object):
    def arrangeCoins(self, n):
        """
        binary search
        Time complexity : O(logN).
        Space complexity : O(1)
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

    def arrangeCoins_math(self, n):
        """
        math
        Time complexity : O(logN).
        Space complexity : O(1)
        :type n: int
        :rtype: int
        """
        return (int)((2 * n + 0.25)**0.5 - 0.5)

if __name__ == "__main__":
    solution = Solution()
    print(solution.arrangeCoins(8))
