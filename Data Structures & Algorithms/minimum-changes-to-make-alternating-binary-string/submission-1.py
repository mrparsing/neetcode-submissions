class Solution:
    def minOperations(self, s: str) -> int:
        res0, res1 = 0, 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                res0 += 1
            else:
                res1 += 1
        return min(res0, res1)