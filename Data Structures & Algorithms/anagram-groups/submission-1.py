class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        listAnagram = []

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            hashmap[str(freq)].append(s)
        
        for v in hashmap.values():
            listAnagram.append(v)
        return listAnagram