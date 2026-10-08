class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        x, y, z, w = 0, 0, float("infinity"), float("infinity")

        for n in nums:
            if n > x:
                y = x
                x = n
            elif n > y:
                y = n
            
            if n < z:
                w = z
                z = n
            elif n < w:
                w = n
        
        return (x * y) - (z * w)