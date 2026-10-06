class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1
            hashmap[tuple(key)].append(s)
        
        return [v for v in hashmap.values()]