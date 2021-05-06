class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        time O(n^2)
        space O(n^2)
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        dp = [[0] * (len(text2) + 1) for _ in range((len(text1) + 1))]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]

    def longestCommonSubsequence_recursion(self, text1, text2):  #TLE
        return self.helper(text1, text2, 0, 0)

    def helper(self, s1, s2, i, j):
        if len(s1) == i or len(s2) == j:
            return 0
        if s1[i] == s2[j]:
            return 1 + self.helper(s1, s2, i + 1, j + 1)
        else:
            return max(self.helper(s1, s2, i + 1, j), self.helper(s1, s2, i, j + 1))

    def longestCommonSubsequence_recursion_memo(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper1(s1, s2, 0, 0, memo)

    def helper1(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper1(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper1(s1, s2, i + 1, j, memo),
                    self.helper1(s1, s2, i, j + 1, memo),
                )
        return memo[i][j]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence("abcba", "abcbcba"))