class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)
        word = "balon"

        for i in range(len(text)):
            if text[i] in word:
                hashmap[text[i]] += 1
        
        if len(hashmap) < 5:
            return 0

        hashmap["l"] //= 2
        hashmap["o"] //= 2
        return min(hashmap.values())
        