class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd = 0
        res = 0
        has_odd = False

        for v in count.values():
            if v % 2 == 0:
                res += v
            else:
                res += (v - 1)
                has_odd = True
        
        if has_odd: res += 1

        return res