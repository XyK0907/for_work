class Solution(object):
    def maxProfit(self, prices):
        """
        time O(n)
        space O(1)
        :type prices: List[int]
        :rtype: int
        """
        prev, later = 0, 1
        sumprofit = 0
        while later < len(prices):
            if prices[later] > prices[prev]:
                sumprofit += prices[later] - prices[prev]
            prev += 1
            later += 1
        return sumprofit

    # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
