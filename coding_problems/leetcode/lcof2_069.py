from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                return i
        return 0


class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


for name in ['Solution', 'Solution2']:
    solution = globals()[name]()
    assert 1 == solution.peakIndexInMountainArray([0,1,0])
    assert 2 == solution.peakIndexInMountainArray([1,3,5,4,2])
    assert 1 == solution.peakIndexInMountainArray([0,10,5,2])
    assert 2 == solution.peakIndexInMountainArray([3,4,5,1])
    assert 2 == solution.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])
