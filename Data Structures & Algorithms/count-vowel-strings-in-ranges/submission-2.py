class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a','e','i','o','u'}
        pref = [0] * (len(words)+1)

        for i, w in enumerate(words):
            is_vowel_string = 1 if w[0] in vowel and w[-1] in vowel else 0
            pref[i+1] = pref[i] + is_vowel_string

        res = []
        for q in queries:
            start, end = q
            res.append(pref[end+1] - pref[start])
        return res