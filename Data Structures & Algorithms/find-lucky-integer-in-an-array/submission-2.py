class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        res = -1
        for num in hashmap:
            if num == hashmap[num]:
                res = max(res, num)
        return res