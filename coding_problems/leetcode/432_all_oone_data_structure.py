import collections


class Node:
    def __init__(self, val=0, key='', left=None, right=None):
        self.keys = set()
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append((cur.keys, cur.val))
            cur = cur.right
        return str(a)


class AllOne:

    def __init__(self):
        self.nodes = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            val = 1
            pre = self.head
        else:
            node = self.nodes[key]
            node.keys.discard(key)
            val = 1 + node.val
            pre = node
        if pre.right.val == val:
            node = pre.right
        else:
            node = Node(val)
            node.left = pre
            node.right = pre.right
            pre.right.left = node
            pre.right = node
        node.keys.add(key)
        self.nodes[key] = node
        if pre != self.head and not pre.keys:
            pre.left.right, pre.right.left = pre.right, pre.left

    def dec(self, key: str) -> None:
        next = self.nodes[key]
        next.keys.discard(key)
        val = next.val - 1
        if val == 0:
            self.nodes.pop(key)
        else:
            if next.left.val == val:
                node = next.left
            else:
                node = Node(val)
                node.left = next.left
                node.right = next
                next.left = node
                node.left.right = node
            node.keys.add(key)
            self.nodes[key] = node
        if not next.keys:
            next.left.right, next.right.left = next.right, next.left

    def getMaxKey(self) -> str:
        for i in self.tail.left.keys:
            return i
        return ''

    def getMinKey(self) -> str:
        for i in self.head.right.keys:
            return i
        return ''


# Your AllOne object will be instantiated and called as such:
allone = AllOne()
# print(allone.head)
allone.inc('hello')
allone.inc('hello')
print(allone.head)
assert 'hello' == allone.getMaxKey()
assert 'hello' == allone.getMinKey()
allone.inc('leet')
assert 'hello' == allone.getMaxKey()
assert 'leet' == allone.getMinKey()
print(allone.head)
allone.dec('hello')
print(allone.head)
allone.dec('hello')
print(allone.head)
assert 'leet' == allone.getMinKey()
assert 'leet' == allone.getMaxKey()
