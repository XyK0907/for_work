class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = {0, 1, 2, 5, 6, 8, 9}
        res = 0
        for i in range(1, N + 1):
            pos = set(map(int, str(i)))
            if pos.issubset({0, 1, 8}):
                continue
            if pos.issubset(digits):
                res += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.rotatedDigits(25))
