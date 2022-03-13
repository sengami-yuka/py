class CQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        if self.b:
            return self.b.pop()
        return -1


obj = CQueue()
for i in range(10):
    obj.appendTail(i)
print(obj.a, obj.b)
for i in range(10):
    param_2 = obj.deleteHead()
    print(param_2)
