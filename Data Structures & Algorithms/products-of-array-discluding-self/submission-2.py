class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * (len(nums))

        for i in range(1, len(nums)):
            product[i] *= (nums[i-1] * product[i-1])
        
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] = product[i] * right_product
            right_product *= nums[i]
        return product