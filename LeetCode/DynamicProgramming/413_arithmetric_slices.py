class Solution(object):
    def numberOfArithmeticSlices_bruteforce(self, A): #mei xie chu lai
        """
        time O(n^2)
        space O(1)
        :type A: List[int]
        :rtype: int
        """
        count = 0
        for s in range(len(A) - 2):
            d = A[s + 1] - A[s]
            for e in range(s + 2, len(A)):
                if A[e] - A[e - 1] == d:
                    count += 1
                else:
                    break
        return count


    def numberOfArithmeticSlices_dp(self, A): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :param A:
        :return:
        """
        dp = [0] * len(A)
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                sum += dp[i]
        return sum

    def numberOfArithmeticSlices_dp_better(self, A): #mei xie chu lai
        """
        time O(n)
        space O(1)
        :param A:
        :return:
        """
        dp = 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                sum += dp
            else:
                dp = 0
        return sum