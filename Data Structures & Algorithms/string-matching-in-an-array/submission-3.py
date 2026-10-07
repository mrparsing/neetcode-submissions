class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        output = []

        for i in range(len(words)-1):
            current = words[i]
            for j in range(i+1, len(words)):
                word = words[j]
                if current in word and current not in output:
                    output.append(current)
        return output