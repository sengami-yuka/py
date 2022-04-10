from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                else:
                    break
        return dp[target]


solution = Solution()
ans = solution.combinationSum4([1,2,3], 4)
assert ans == 7, ans

ans = solution.combinationSum4([9], 3)
assert ans == 0, ans

ans = solution.combinationSum4([1,2,3], 5)
assert ans == 13, ans

ans = solution.combinationSum4([1,2,3], 6)
assert ans == 24, ans

ans = solution.combinationSum4([4,2,1], 32)
assert ans == 39882198, ans

ans = solution.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10)
assert ans == 9, ans
