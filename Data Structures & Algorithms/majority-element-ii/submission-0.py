class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        res = []
        target = math.floor(len(nums) / 3)

        for k, v in freq.items():
            if v > target:
                res.append(k)
        return res