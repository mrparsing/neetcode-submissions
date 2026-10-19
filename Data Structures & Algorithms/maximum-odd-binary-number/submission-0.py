class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        res = [0] * len(s)
        i = 0
        res[-1] = 1
        count["1"] -= 1

        while count["1"] > 0 and i < len(s)-1:
            res[i] = 1
            count["1"] -= 1
            i += 1
        return "".join(str(i) for i in res)