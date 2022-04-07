import math
from collections import defaultdict
from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0] * (6 * n + 1) for _ in range(n)]
        for i in range(1, 7):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1) + 1):
                for k in range(1, 7):
                    if j > k:
                        dp[i][j] += dp[i - 1][j - k]
        d = math.pow(6, n)
        return [x / d for x in dp[-1] if x > 0]


class Solution2:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j]
            dp = tmp
        d = math.pow(6, n)
        # print(dp)
        return [x / d for x in dp]


solution = Solution2()
ans = solution.dicesProbability(1)

# assert ans == [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667], ans

ans = solution.dicesProbability(2)
# assert ans == [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778], ans

ans = solution.dicesProbability(3)
