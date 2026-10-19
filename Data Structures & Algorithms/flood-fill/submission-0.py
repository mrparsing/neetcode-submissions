class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.originalColor = image[sr][sc]
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != self.originalColor or (i, j) in visit:
                return
            else:
                visit.add((i, j))
                image[i][j] = color
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        dfs(sr, sc)

        return image