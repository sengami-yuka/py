class Solution:
    def maximumDifference(self, nums):
        ans, premin = -1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]
        return ans


s = Solution()
assert 4 == s.maximumDifference([7,1,5,4])
assert -1 == s.maximumDifference([9,4,3,2])
assert 9 == s.maximumDifference([1,5,2,10])
