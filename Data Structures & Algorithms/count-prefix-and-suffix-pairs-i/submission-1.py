class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counterWord = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    counterWord += 1
        return counterWord

    def isPrefixAndSuffix(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        if len1 > len2:
            return False
        
        for i in range(len1):
            if str1[i] != str2[i]:
                return False
        
        offset = len2 - len1
        for i in range(len1):
            if str1[i] != str2[offset + i]:
                return False
        return True