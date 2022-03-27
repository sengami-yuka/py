import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1 = len(word1)
        L2 = len(word2)
        DP = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)]
        for j in range(1, L2 + 1):
            DP[0][j] = j
        for i in range(1, L1 + 1):
            DP[i][0] = i
        for i in range(L1):
            for j in range(L2):
                if word1[i] == word2[j]:
                    DP[i + 1][j + 1] = DP[i][j]
                else:
                    DP[i + 1][j + 1] = 1 + min(DP[i + 1][j], DP[i][j + 1], DP[i][j])
        return DP[-1][-1]


solution = Solution()
ans = solution.minDistance('horse', 'ros')
assert ans == 3, ans

ans = solution.minDistance('intention', 'execution')
assert ans == 5, ans
