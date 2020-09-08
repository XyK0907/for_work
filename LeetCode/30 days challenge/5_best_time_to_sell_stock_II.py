class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sum_profit += prices[i+1]-prices[i]
            else:
                continue
        return sum_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,6,4,3,1]))