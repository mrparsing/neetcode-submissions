class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = defaultdict(int)

        for c in s:
            hashmap[c] += 1
        
        max_odd = max((x for x in hashmap.items() if x[1] % 2 != 0), key=lambda x: x[1])
        min_even = min((x for x in hashmap.items() if x[1] % 2 == 0), key=lambda x: x[1])

        return max_odd[1] - min_even[1]