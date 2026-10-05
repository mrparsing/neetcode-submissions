class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        l = 0
        max_lenght = 0

        for r in range(len(s)):
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            char_index[s[r]] = r

            max_lenght = max(max_lenght, r - l + 1)
        return max_lenght