import collections


class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key, True)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key, True)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(False)


class Node:
    def __init__(self, key=-1, value=0):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.move_to_end(node)
        else:
            node = Node(key, value)
            self.d[key] = node
            self.move_to_end(node)
            if len(self.d) > self.capacity:
                node = self.popleft()
                del self.d[node.key]

    def move_to_end(self, node):
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        node.right = self.tail
        node.left = self.tail.left
        self.tail.left.right = node
        self.tail.left = node

    def popleft(self):
        node = self.head.right
        self.head.right = node.right
        node.right.left = self.head
        return node


lRUCache = LRUCache2(2)
# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
# [null,null,null,null,null,-1,3]
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
print(lRUCache.get(1))
print(lRUCache.get(2))
