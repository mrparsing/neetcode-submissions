class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        i = 0
        while i < len(s):
            if pattern[i] in hashmap and hashmap[pattern[i]] != s[i]:
                return False
            elif pattern[i] not in hashmap and s[i] in hashmap.values():
                return False
            hashmap[pattern[i]] = s[i]
            i += 1
        return True