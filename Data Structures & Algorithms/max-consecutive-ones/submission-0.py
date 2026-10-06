class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        i = 0

        while i < len(nums):
            tmp = 0
            while i < len(nums) and nums[i] == 1:
                tmp += 1
                i += 1
            max_cons = max(max_cons, tmp)
            i += 1
        return max_cons