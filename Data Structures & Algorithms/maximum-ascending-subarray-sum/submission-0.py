class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        i = 0

        while i < len(nums):
            j = i + 1
            currSum = nums[j-1]
            while j < len(nums) and nums[j-1] < nums[j]:
                currSum += nums[j]
                j += 1
            maxSum = max(maxSum, currSum)
            i += 1
        return maxSum