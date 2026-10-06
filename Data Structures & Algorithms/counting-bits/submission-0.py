class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(self.count(i))
        
        return output

    def count(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res