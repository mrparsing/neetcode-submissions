class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for w in words:
            for c in w:
                count[c] += 1

        return all(freq % len(words) == 0 for freq in count.values())