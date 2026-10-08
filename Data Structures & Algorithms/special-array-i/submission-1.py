class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return True
        
        i = 1

        while i < len(nums):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
            i += 1
        return True