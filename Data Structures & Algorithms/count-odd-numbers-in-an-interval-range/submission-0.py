class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lenght = high - low + 1
        count = lenght // 2
        
        if lenght % 2 and low % 2:
            count += 1
        return count