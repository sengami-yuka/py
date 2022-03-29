from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = cnt = 0
        for num in nums:
            cnt += num == 0
            if cnt > k:
                cnt -= nums[left] == 0
                left += 1
        return len(nums) - left
