class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N / 2):
            for j in range(i, N - 1 - i):
                matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i] = \
                    matrix[-j-1][i], matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1]


s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(matrix)
assert matrix == [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(matrix)
assert matrix == [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
