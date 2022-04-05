from typing import List
from bisect import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res


class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


class Solution4:  # with path
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = []
        path_idx = [0] * n
        for i, num in enumerate(nums):
            if not d or num > d[-1]:
                path_idx[i] = len(d)
                d.append(num)
            else:
                idx = bisect_left(d, num)
                d[bisect_left(d, num)] = num
                path_idx[i] = idx

        nd = len(d)
        path = [0] * nd
        j = nd - 1
        for i in reversed(range(n)):
            if path_idx[i] == j:
                path[j] = nums[i]
                j -= 1
        print(path)
        return len(d)


solution = Solution4()
ans = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
assert ans == 4, ans

ans = solution.lengthOfLIS([10,9,2,5,3,7,101,18,19])
assert ans == 5, ans

ans = solution.lengthOfLIS([0,1,0,3,2,3])
assert ans == 4, ans

ans = solution.lengthOfLIS([7,7,7,7,7,7,7])
assert ans == 1, ans

ans = solution.lengthOfLIS([4,10,4,3,8,9])
assert ans == 3, ans

ans = solution.lengthOfLIS([1,23,4,5,33,8,90,91])
assert ans == 6, ans

ans = solution.lengthOfLIS([0,8,4,12,2,13,7])
assert ans == 4, ans

ans = solution.lengthOfLIS([0,8,9,12,2,3,4,13,7])
assert ans == 5, ans
