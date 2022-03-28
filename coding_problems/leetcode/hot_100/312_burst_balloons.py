from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = nums[i] * nums[k] * nums[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)

        return dp[0][-1]


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        L = len(nums)

        dp = [[0] * L for _ in range(L)]

        for n in range(2, L):
            for i in range(L - n):
                m = 0
                j = i + n
                for k in range(i + 1, j):
                    a = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    if a > m:
                        m = a
                dp[i][j] = m

        return dp[0][-1]


solution = Solution2()
ans = solution.maxCoins([3,1,5,8])
assert ans == 167, ans

ans = solution.maxCoins([1,5])
assert ans == 10, ans
