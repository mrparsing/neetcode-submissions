class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for n in nums:
            tmp = 0
            if n-1 not in nums_set:
                i = n
                while i in nums_set:
                    nums_set.remove(i)
                    i += 1
                    tmp += 1
            res = max(res, tmp)
        return res