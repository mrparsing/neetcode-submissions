class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = (-1 + math.sqrt(1 + 8*n)) // 2

        return int(r)