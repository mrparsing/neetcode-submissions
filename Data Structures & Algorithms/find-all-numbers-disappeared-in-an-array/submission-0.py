class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = [i for i in range(1, len(nums)+1)]

        for i in range(len(nums)):
            if nums[i] in output:
                output.remove(nums[i])
        return output