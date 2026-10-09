class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                res = max(res, int(num[i]))

        return str(res) * 3 if res != -1 else ""
