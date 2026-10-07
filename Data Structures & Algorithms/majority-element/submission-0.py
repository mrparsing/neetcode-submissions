class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        return max(hashmap.items(), key=lambda x: x[1])[0]