class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        have = set(allowed)
        res = 0

        for w in words:
            good = True
            for c in w:
                if c not in have:
                    good = False
                    break
            if good:
                res += 1
        return res