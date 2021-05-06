"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2

示例 2：

输入：n = 7
输出：21

示例 3：

输入：n = 0
输出：1

提示：

    0 <= n <= 100
"""
class Solution(object):
    def numWays_recursion(self, n):
        """
        overtime
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        return self.numWays(n - 1) + self.numWays(n - 2)

    def numWays_another_recur(self, n):
        """
        记忆化递归法
        time O(n)
        space O(n)
        overtime
        :type n: int
        :rtype: int
        """
        dic = {1: 1, 2: 2}
        if n == 1 or n == 2:
            return n
        for i in range(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n]

    def numWays_fabonacci(self, n):
        """
        time O(n)
        space O(n)
        overtime
        :type n: int
        :rtype: int
        """
        a = b = 1
        for _ in range(n):
            a, b = b, a+b
        return a




if __name__ == '__main__':
    solution = Solution()
    print(solution.numWays(5))