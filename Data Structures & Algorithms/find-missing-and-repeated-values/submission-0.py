class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        #row = (nums[i] - 1) // len(nums)
        #col = (nums[i] - 1) % 2  len(nums)

        for row in range(n):
            for col in range(n):
                index_r = (abs(grid[row][col]) - 1) // n
                index_c = (abs(grid[row][col]) - 1) % n
                if grid[index_r][index_c] > 0:
                    grid[index_r][index_c] = -grid[index_r][index_c]
        
        missing = -1
        for row in range(n):
            for col in range(n):
                if grid[row][col] > 0:
                    missing = [grid[row][col], row * n + col+ 1]
        return missing