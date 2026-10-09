class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = set()

        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                good.add(num[i]+num[i-1]+num[i-2])
                i += 3
        
        return max(good) if len(good) > 0 else ""
