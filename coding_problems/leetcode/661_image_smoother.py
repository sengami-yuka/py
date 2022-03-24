from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = img[i][j]
                c = 1
                if i > 0:
                    ans[i][j] += img[i - 1][j]
                    c += 1
                    if j > 0:
                        ans[i][j] += img[i - 1][j - 1]
                        c += 1
                    if j < n - 1:
                        ans[i][j] += img[i - 1][j + 1]
                        c += 1
                if i < m - 1:
                    ans[i][j] += img[i + 1][j]
                    c += 1
                    if j > 0:
                        ans[i][j] += img[i + 1][j - 1]
                        c += 1
                    if j < n - 1:
                        ans[i][j] += img[i + 1][j + 1]
                        c += 1
                if j > 0:
                    ans[i][j] += img[i][j - 1]
                    c += 1
                if j < n - 1:
                    ans[i][j] += img[i][j + 1]
                    c += 1
                ans[i][j] //= c
        return ans
