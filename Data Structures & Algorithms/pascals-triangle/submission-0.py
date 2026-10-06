class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1, 1])
            else:
                row = [1] * (i+1)
                for j in range(1, len(row) - 1):
                    row[j] = triangle[i-1][j] + triangle[i-1][j-1]
                triangle.append(row)
        return triangle