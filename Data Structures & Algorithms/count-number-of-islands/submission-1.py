class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(x, y):
            stack = [(x, y)]
            visited.add((x, y))

            while stack:
                curr = stack.pop()

                for d in direction:
                    new_x = curr[0] + d[0]
                    new_y = curr[1] + d[1]

                    if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and grid[new_x][new_y] == "1" and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        stack.append((new_x, new_y))

        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and tuple((x, y)) not in visited:
                    dfs(x, y)
                    counter += 1

        return counter