class Solution:
    def maxDepth(self, s: str) -> int:
        maxNested = 0
        tmp = 0
        i = 0

        while i < len(s):
            if s[i] == "(":
                tmp += 1
            elif s[i] == ")":
                maxNested = max(maxNested, tmp)
                tmp -= 1
            i += 1
        return maxNested