class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if len(prices) > 1:
            chocolate1 = prices.pop(0)
            chocolate2 = prices.pop(0)
            leftover = money - (chocolate2 + chocolate1)

            return leftover if leftover >= 0 else money
        
        return money