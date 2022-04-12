import random


class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        idx = len(self.values)
        self.d[val] = idx
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        idx = self.d[val]
        del self.d[val]
        if idx == len(self.values) - 1:
            self.values.pop()
        else:
            tmp = self.values.pop()
            self.values[idx] = tmp
            self.d[tmp] = idx
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
cmds = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
params = [[],[1],[2],[2],[],[1],[2],[]]
s = RandomizedSet()
for cmd, param in zip(cmds[1:], params[1:]):
    out = getattr(s, cmd)(*param)
    print(out)
    print(s.d)
