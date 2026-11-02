class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for n in nums_set:
            if n-1 not in nums_set:
                i = 1
                while (n + i) in nums_set:
                    i += 1
                res = max(res, i)
        return res