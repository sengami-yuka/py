import collections
import bisect


class RecentCounter:
    def __init__(self):
        self.data = collections.deque()

    def ping(self, t: int) -> int:
        self.data.append(t)
        target = t - 3000
        while self.data[0] < target:
            self.data.popleft()
        return len(self.data)


class RecentCounter2:
    def __init__(self):
        self.data = []
        self.left = 0

    def ping(self, t: int) -> int:
        self.data.append(t)
        self.left = bisect.bisect_left(self.data, t - 3000, self.left)
        return len(self.data) - self.left


recentCounter = RecentCounter()
assert 1 == recentCounter.ping(1)     # requests = [1]，范围是 [-2999,1]，返回 1
assert 2 == recentCounter.ping(100)   # requests = [1, 100]，范围是 [-2900,100]，返回 2
assert 3 == recentCounter.ping(3001)  # requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
assert 3 == recentCounter.ping(3002)  # requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
assert 1 == recentCounter.ping(9999)
assert 2 == recentCounter.ping(10000)
