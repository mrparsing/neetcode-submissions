import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k != 0:
            g = -heapq.heappop(gifts)
            square = math.floor(sqrt(g))
            heapq.heappush(gifts, -square)
            k -= 1
        
        return sum(-g for g in gifts)