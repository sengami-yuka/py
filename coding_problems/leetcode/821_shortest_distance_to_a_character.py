from typing import List
from collections import deque


class Solution:  # bfs
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n
        q = deque()
        for i, ch in enumerate(s):
            if ch == c:
                q.append(i)
        num = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if num < ans[i]:
                    ans[i] = num
                    if i - 1 >= 0:
                        q.append(i - 1)
                    if i + 1 < n:
                        q.append(i + 1)
            num += 1
        return ans


class Solution2:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        il = []
        for i, ch in enumerate(s):
            if ch == c:
                il.append(i)
        for i in range(il[0]):
            ans[i] = il[0] - i
        for i in range(il[-1] + 1, n):
            ans[i] = i - il[-1]
        if len(il) > 1:
            left, right = 0, 1
            for i in range(il[0] + 1, il[-1]):
                if i == il[right]:
                    left, right = right, right + 1
                else:
                    ans[i] = min(i - il[left], il[right] - i)
        return ans


class Solution3:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n
        last = -1
        for i, ch in enumerate(s):
            if ch == c:
                ans[i] = 0
                last = i
            elif last > -1:
                ans[i] = i - last

        last = n
        for i in reversed(range(n)):
            if s[i] == c:
                ans[i] = 0
                last = i
            elif last < n:
                ans[i] = min(ans[i], last - i)

        return ans


class Solution4:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n

        idx = -n
        for i, ch in enumerate(s):
            if ch == c:
                idx = i
            ans[i] = i - idx

        idx = 2 * n
        for i in reversed(range(n)):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans


solution = Solution4()
ans = solution.shortestToChar('loveleetcode', 'e')
assert ans == [3,2,1,0,1,0,0,1,2,2,1,0], ans

ans = solution.shortestToChar('aaab', 'b')
assert ans == [3,2,1,0], ans
