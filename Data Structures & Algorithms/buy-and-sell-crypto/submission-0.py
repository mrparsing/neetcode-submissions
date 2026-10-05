class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            buy = prices[i]

            k = i+1
            while k < len(prices):
                profit = prices[k] - buy
                max_profit = max(max_profit, profit)
                print(profit, max_profit)

                k += 1
        return max_profit