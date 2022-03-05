class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target - n] = i
        return []
