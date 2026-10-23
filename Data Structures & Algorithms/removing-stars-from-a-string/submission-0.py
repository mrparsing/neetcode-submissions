class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != '*':
                stack.append(c)
            else:
                if len(stack) > 0:
                    stack.pop()
        return "".join(stack)