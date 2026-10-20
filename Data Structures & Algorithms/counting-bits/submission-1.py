class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            res.append(self.count(i))
        
        return res

    def count(self, i):
        out = 0
        while i > 0:
            i = i & (i - 1)
            out += 1
        return out