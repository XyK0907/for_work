class Solution(object):
    def findLongestChain(self, pairs): #my solution
        """
        time O(n^2)
        space O(n)
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[0])
        if not pairs:
            return 0
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def findLongestChain_greedy(self, pairs): #mei zuo chu lai
        """
        time O(nlogn), sorting logn, rest linear
        space O(n), cur & ans O(1), sorting O(n)
        :param pairs:
        :return:
        """
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=lambda x: x[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestChain([[1,2], [2,3], [3,4]]))
    print(solution.findLongestChain([[1,2], [5,6], [3,4]]))