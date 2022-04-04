from heapq import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        s = set()
        ans = 0
        for _ in range(n):
            ans = heappop(h)
            two = ans * 2
            if two not in s:
                heappush(h, two)
                s.add(two)
            three = ans * 3
            if three not in s:
                heappush(h, three)
                s.add(three)
            five = ans * 5
            if five not in s:
                heappush(h, five)
                s.add(five)
        return ans


class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


solution = Solution()
ans = solution.nthUglyNumber(10)
assert ans == 12, ans
