# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(node):
            if node:
                dfs(node.right)
                self.data.append(node.val)
                dfs(node.left)
        self.data = []
        dfs(root)

    def next(self) -> int:
        if self.data:
            return self.data.pop()
        return -1

    def hasNext(self) -> bool:
        return len(self.data) > 0


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.data = []
        self.node = root

    def next(self) -> int:
        while self.node:
            self.data.append(self.node)
            self.node = self.node.left
        self.node = self.data.pop()
        ans = self.node.val
        self.node = self.node.right
        return ans

    def hasNext(self) -> bool:
        return self.node is not None or len(self.data) > 0


# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
obj = BSTIterator2(root)
params = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
expect = [None, 3, 7, True, 9, True, 15, True, 20, False]
for i in range(1, len(params)):
    out = obj.__getattribute__(params[i])()
    assert out == expect[i], (out, expect[i])
