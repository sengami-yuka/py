from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        heapq.heapify(self.heap)
        for _ in range(len(nums) - k):
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
ipt1 = ["KthLargest", "add", "add", "add", "add", "add"]
ipt2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
out = [None, 4, 5, 5, 8, 8]
obj = KthLargest(*ipt2[0])
for i in range(1, len(ipt1)):
    ans = obj.__getattribute__(ipt1[i])(*ipt2[i])
    assert ans == out[i], (i, ans, out[i])
