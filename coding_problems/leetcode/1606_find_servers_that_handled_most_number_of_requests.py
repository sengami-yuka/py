from heapq import *
from typing import List
from collections import *
import bisect


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = [0] * k
        reqs = [0] * k
        max_req = 0
        ans = []
        for i, (start, t) in enumerate(zip(arrival, load)):
            j = -1
            for ii in range(k):
                if servers[(ii + i) % k] <= start:
                    j = (ii + i) % k
                    break
            if j > -1:
                servers[j] = start + t
                reqs[j] += 1
                if reqs[j] > max_req:
                    ans = [j]
                    max_req = reqs[j]
                elif reqs[j] == max_req:
                    ans.append(j)
        return ans


class Solution2:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        ans = []
        maxRequest = 0
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                bisect.insort_left(available, busy[0][1])
                heappop(busy)
            if len(available) == 0:
                continue
            j = bisect.bisect_left(available, i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            del available[bisect.bisect_left(available, id)]
            if requests[id] > maxRequest:
                maxRequest = requests[id]
                ans = [id]
            elif requests[id] == maxRequest:
                ans.append(id)
        return ans


class Solution3:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        ans = []
        maxRequest = 0
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heappop(busy)
                heappush(available, i + (id - i) % k)
            if available:
                id = heappop(available) % k
                requests[id] += 1
                if requests[id] > maxRequest:
                    maxRequest = requests[id]
                    ans = [id]
                elif requests[id] == maxRequest:
                    ans.append(id)
                heappush(busy, (start + t, id))
        return ans


solution = Solution3()
ans = solution.busiestServers(3, [1,2,3,4,5], [5,2,3,3,3])
assert ans == [1], ans

ans = solution.busiestServers(3, [1,2,3,4], [1,2,1,2])
assert ans == [0], ans

ans = solution.busiestServers(3, [1,2,3], [10,12,11])
assert ans == [0,1,2], ans

ans = solution.busiestServers(3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2])
assert ans == [1], ans

ans = solution.busiestServers(1, [1], [1])
assert ans == [0], ans
