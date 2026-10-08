class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        mancante = -1
        for n in nums:
            abs_value = abs(n)
            index = abs_value - 1

            if nums[index] < 0:
                duplicate = abs_value
            else:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                mancante = i + 1
                break
                
        return [duplicate, mancante]