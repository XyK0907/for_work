class Solution(object):
    def maxProfit(self,prices): #mei xie chu lai
        """
        Kadane's algorithm
        Time O(n)
        space O(1)
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit_brute_force(self, prices):
        """
        Brute Force
        Time O(n^2)
        space O(1)
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit




if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([3,2,6,5,0,3]))
    #print(solution.maxProfit([7, 6, 4, 3, 1]))