from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num)
        return dp[-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = max(dp1, dp2 + num), dp1
        return dp1


solution = Solution2()
ans = solution.rob([1,2,3,1])
assert ans == 4, ans

ans = solution.rob([2,7,9,3,1])
assert ans == 12, ans
