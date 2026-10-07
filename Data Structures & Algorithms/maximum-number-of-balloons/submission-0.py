class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)
        word = "balloon"

        for i in range(len(text)):
            hashmap[text[i]] += 1
        
        i = 0
        count = 0
        while i < len(word) and hashmap[word[i]] > 0:
            hashmap[word[i]] -= 1
            if i == len(word)-1 and hashmap[word[i]] >= 0:
                count += 1
                i = 0
            i += 1
        return count