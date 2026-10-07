class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        s = s.split()
        mapped_words = set()

        if len(s) != len(pattern):
            return False
        
        for char, word in zip(pattern, s):
            if char in hashmap:
                if hashmap[char] != word:
                    return False
            else:
                if word in mapped_words:
                    return False
            hashmap[char] = word
            mapped_words.add(word)
        return True