class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_char = defaultdict(int)
        l = 0
        max_sequence = 0

        for r in range(len(s)):
            count_char[s[r]] += 1
        
            while k < (r - l + 1) - max(count_char.values()):
                count_char[s[l]] -= 1
                l += 1
            
            max_sequence = max(max_sequence, (r - l + 1))
        
        return max_sequence