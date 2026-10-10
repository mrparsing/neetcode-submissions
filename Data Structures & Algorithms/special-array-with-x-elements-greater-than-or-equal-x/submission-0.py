class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums)+1)
        for num in nums:
            index = min(num, len(nums))
            count[index] += 1
        
        total = 0
        print(count)
        for i in range(len(nums), -1, -1):
            total += count[i]
            if total == i:
                return total
        return -1