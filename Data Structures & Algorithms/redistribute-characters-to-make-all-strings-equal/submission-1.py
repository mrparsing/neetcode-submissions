class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for w in words:
            for c in w:
                count[c] += 1

        for v in count.values():
            if v % len(words) != 0:
                return False
        return True