class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums)+1)
        prefix_sum = 0
        res = 0
        i = 1
        for n in nums:
            prefix_sum += n
            prefix[i] = prefix_sum
            i+=1

        for i in range(1, len(prefix)):
            for j in range(0, i):
                curr_sum = prefix[i] - prefix[j]
                if curr_sum % k == 0:
                    res += 1
        return res
