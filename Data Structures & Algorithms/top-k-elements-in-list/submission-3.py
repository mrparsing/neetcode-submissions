class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for elem, val in count:
            res.append(elem)
            k -= 1
            if k == 0:
                break
        return res