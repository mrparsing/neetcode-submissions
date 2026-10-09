class Solution:
    def maxScore(self, s: str) -> int:
        # score = left_zero + right_ones
        # right_ones = total_ones - left_ones
        # score = left_zero + total_ones - left_ones

        res = -1
        left_zero, left_ones = 0, 0

        if s[0] == "0":
            left_zero += 1
        else:
            left_ones += 1

        for i in range(1, len(s)):
            res = max(res, left_zero - left_ones)
            if s[i] == "0":
                left_zero += 1
            else:
                left_ones += 1
        return res + left_ones