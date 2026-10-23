class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p, q = 0, 0

        while p < len(pushed) and q < len(popped):
            stack.append(pushed[p])
            while stack and q < len(popped) and stack[-1] == popped[q]:
                stack.pop()
                q += 1
            p += 1
        return True if len(stack) == 0 else False