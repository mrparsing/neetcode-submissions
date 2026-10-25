class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indices = {}

        for i, c in enumerate(order):
            indices[c] = i
        
        sDict = defaultdict(int)
        for c in s:
            sDict[c] += 1
        
        res = []
        print(sDict.items())
        for c in order:
            if c in sDict:
                res.append(c * sDict[c])
                del sDict[c]
        
        for c in sDict:
            res.append(c * sDict[c])
            
        
        return "".join(res)