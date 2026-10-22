class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        bin_arr = [0] * len(words)
        vowel = {'a','e','i','o','u'}

        for i, w in enumerate(words):
            if w[0] in vowel and w[-1] in vowel:
                bin_arr[i] = 1
            else:
                bin_arr[i] = 0
        
        res = []
        print(bin_arr)
        for q in queries:
            start, end = q
            res.append(sum(bin_arr[start:end+1]))
        return res