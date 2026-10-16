class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        res = [0] * n
        for i in range(n):
            s = 0
            for j in range(1, abs(k) + 1):
                s += code[(i + (j if k > 0 else -j)) % n]
            res[i] = s
        return res