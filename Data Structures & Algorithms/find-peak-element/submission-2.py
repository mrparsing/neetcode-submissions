class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0 and i < len(nums) - 1 and nums[i] > nums[i+1]:
                return i
            elif i < len(nums) - 1 and nums [i-1] < nums[i] > nums[i+1]:
                return i
            elif i == len(nums)-1:
                return i