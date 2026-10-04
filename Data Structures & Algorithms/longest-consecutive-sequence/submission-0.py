class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_lenght = 0

        for num in nums:
            output = 1

            if num - 1 not in nums:
                prox = num + 1
                while prox in nums:
                    output += 1
                    prox = prox + 1
            max_lenght = max(max_lenght, output)
        return max_lenght