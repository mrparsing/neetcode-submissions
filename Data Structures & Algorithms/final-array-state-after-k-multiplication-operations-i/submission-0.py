class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            value, i = heapq.heappop(heap)
            heapq.heappush(heap, (value*multiplier, i))
        
        res = [0] * len(nums)
        for val, i in heap:
            res[i] = val
        return res