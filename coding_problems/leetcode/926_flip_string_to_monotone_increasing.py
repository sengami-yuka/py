
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = dp = 0
        for c in s:
            if c == '0':
                dp = min(dp + 1, one)
            else:
                one += 1
        return dp


solution = Solution()
ans = solution.minFlipsMonoIncr('00110')
assert ans == 1, ans

ans = solution.minFlipsMonoIncr('010110')
assert ans == 2, ans

ans = solution.minFlipsMonoIncr('0110110')
assert ans == 2, ans

ans = solution.minFlipsMonoIncr('0101100')
assert ans == 3, ans

ans = solution.minFlipsMonoIncr('00011000')
assert ans == 2, ans

ans = solution.minFlipsMonoIncr('0101100011')
assert ans == 3, ans

ans = solution.minFlipsMonoIncr('10011111110010111011')
assert ans == 5, ans
