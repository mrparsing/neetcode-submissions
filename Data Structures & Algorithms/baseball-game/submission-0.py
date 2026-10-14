class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                score1 = stack[-1]
                score2 = stack[-2]
                stack.append(score1 + score2)
            elif o == "C":
                stack.pop()
            elif o == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(o))
        return sum(stack)