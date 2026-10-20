class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces_set = set(spaces)
        for i, c in enumerate(s):
            if i in spaces_set:
                res.append(" ")
            res.append(c)
        return "".join(res)