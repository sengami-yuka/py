from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [0] * m
        cols = [0] * n
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0


s = Solution()
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
s.setZeroes(matrix)
assert [
  [1,0,1],
  [0,0,0],
  [1,0,1]
] == matrix

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(matrix)
assert [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
] == matrix
