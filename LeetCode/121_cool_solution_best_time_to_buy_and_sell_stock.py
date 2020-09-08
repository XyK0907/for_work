class Solution(object):
    def maxProfit(self,prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            print(min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit




if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([3,2,6,5,0,3]))
    #print(solution.maxProfit([7, 6, 4, 3, 1]))