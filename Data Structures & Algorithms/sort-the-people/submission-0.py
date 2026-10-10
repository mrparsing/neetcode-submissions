class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}

        for i in range(len(names)):
            hashmap[heights[i]] = names[i]
        
        res = []
        for h in reversed(sorted(heights)):
            res.append(hashmap[h])
        
        return res