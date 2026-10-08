class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)

        a = count1 & count2
        
        for c in ransomNote:
            if c in a:
                a[c] -= 1
            if a[c] < 0 or c not in a:
                return False
        return True