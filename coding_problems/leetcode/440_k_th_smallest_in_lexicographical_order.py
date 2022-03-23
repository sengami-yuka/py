class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps, first, last = 0, cur, cur + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
            print(steps, cur, k)
        return cur


solution = Solution()
ans = solution.findKthNumber(13, 2)
assert ans == 10, ans
#
# ans = solution.findKthNumber(1, 1)
# assert ans == 1, ans
# #
ans = solution.findKthNumber(10, 3)
assert ans == 2, ans
#
ans = solution.findKthNumber(100, 9)
assert ans == 16, ans
#
# ans = solution.findKthNumber(100, 10)
# assert ans == 17, ans
