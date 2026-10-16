class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # [1,2,3,6,7] k = 3
        # [11,16,14]

        res = [0] * len(code)
        for i in range(len(code)):
            s = 0
            for j in range(1, abs(k) + 1):
                s += code[(i + (j if k > 0 else -j)) % len(code)]
            res[i] = s
        return res