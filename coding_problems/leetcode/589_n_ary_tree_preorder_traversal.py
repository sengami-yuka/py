from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            for c in node.children:
                dfs(c)
        ans = []
        dfs(root)
        return ans


class Solution2:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            node = s.pop()
            ans.append(node.val)
            for c in node.children[::-1]:
                s.append(c)
        return ans


solution = Solution2()
root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
assert [1, 3, 5, 6, 2, 4] == solution.preorder(root)
