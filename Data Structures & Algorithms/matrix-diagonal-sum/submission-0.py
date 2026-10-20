class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag = 0

        for i in range(len(mat)):
            diag += (mat[i][i] + mat[len(mat)-i-1][i])
        if len(mat) % 2 != 0:
            diag -= mat[len(mat) // 2][len(mat) // 2]
        return diag