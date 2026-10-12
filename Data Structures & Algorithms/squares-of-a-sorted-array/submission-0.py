class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        res = []

        while i <= j:
            square1 = nums[i]**2
            square2 = nums[j]**2

            if square1 > square2:
                res.append(square1)
                i += 1
            else:
                res.append(square2)
                j -= 1
        res = list(reversed(res))
        return res