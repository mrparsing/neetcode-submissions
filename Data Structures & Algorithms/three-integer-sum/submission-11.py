class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            current = nums[i]

            while left < right:
                threesum = current + nums[left] + nums[right]

                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    output.append([current, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return output