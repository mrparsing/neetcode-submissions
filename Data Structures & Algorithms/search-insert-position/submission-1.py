class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        print(l, r)
        if nums[r] < target:
            return r + 1 if r+1 < len(nums) else len(nums)
        else:
            return r - 1 if r-1 > 0 else 0