class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)

        for a in arr:
            hashmap[a] += 1
        
        lli = 0
        for i, v in hashmap.items():
            if i == v:
                lli = max(lli, i)
        return lli if lli != 0 else -1