class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return True
        
        parity = nums[0] % 2
        i = 1

        while i < len(nums):
            if 1 - parity != nums[i] % 2:
                return False
            parity = 1 - parity
            i += 1
        return True