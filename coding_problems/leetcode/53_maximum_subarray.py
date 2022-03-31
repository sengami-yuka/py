from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur = -10000
        for num in nums:
            cur = max(num, num + cur)
            if cur > ans:
                ans = cur
        return ans
