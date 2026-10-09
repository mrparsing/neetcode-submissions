class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lenght = 0
        have = Counter(chars)

        for w in words:
            curr_w = Counter(w)
            good = True
            for c in curr_w:
                if curr_w[c] > have[c]:
                    good = False
                    break
            if good:
                lenght += len(w)
        return lenght