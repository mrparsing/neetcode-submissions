class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        heap = []

        for val, freq in count.items():
            heapq.heappush(heap, (freq, val))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]