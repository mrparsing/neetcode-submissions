class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        pos = {(0, 0)}

        for c in path:
            if c == "N":
                x += 1
            elif c == "S":
                x -= 1
            elif c == "E":
                y += 1
            elif c == "W":
                y -= 1
            if (x, y) in pos:
                return True
            pos.add((x, y))
        return False