from typing import List
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        a = [i for i, v in enumerate(s) if v == '|']
        for q in queries:
            left = bisect.bisect_left(a, q[0])
            right = bisect.bisect_right(a, q[1]) - 1
            if left < right:
                ans.append(a[right] - a[left] + left - right)
            else:
                ans.append(0)
        return ans


class Solution2:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        length = len(s)
        L = [-1] * length
        R = [-1] * length
        c_map = {}
        idx = -1
        for i, v in enumerate(s):
            if v == '|':
                c_map[i] = len(c_map)
                idx = i
            R[i] = idx
        idx = -1
        for i, v in reversed(list(enumerate(s))):
            if v == '|':
                idx = i
            L[i] = idx
        for i, (x, y) in enumerate(queries):
            left = L[x]
            right = R[y]
            if left != -1 and right != -1 and left >= right:
                ans[i] = right - left + c_map[left] - c_map[right]
        return ans


class Solution3:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans


solution = Solution3()
assert [2,3] == solution.platesBetweenCandles('**|**|***|', [[2,5],[5,9]])
assert [9,0,0,0,0] == solution.platesBetweenCandles('***|**|*****|**||**|*', [[1,17],[4,5],[14,17],[5,11],[15,16]])
