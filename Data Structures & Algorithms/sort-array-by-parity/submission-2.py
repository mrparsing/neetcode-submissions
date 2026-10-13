class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        k = 0
        res = [0] * len(nums)

        while k < len(nums):
            if nums[k] % 2 == 0:
                res[i] = nums[k]
                i += 1
            else:
                res[j] = nums[k]
                j -= 1
            k += 1
        return res