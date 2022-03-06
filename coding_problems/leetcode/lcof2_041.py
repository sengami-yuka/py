import collections


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.data = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        self.data.append(val)
        if len(self.data) > self.size:
            self.total -= self.data.popleft()
        return self.total / len(self.data)


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
print(param_1)
param_1 = obj.next(10)
print(param_1)
param_1 = obj.next(3)
print(param_1)
param_1 = obj.next(5)
print(param_1)

