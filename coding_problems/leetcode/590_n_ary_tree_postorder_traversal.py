from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        def dfs(node):
            if node:
                for c in node.children:
                    dfs(c)
                ans.append(node.val)
        ans = []
        dfs(root)
        return ans


class Solution2:
    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            node = s.pop()
            ans.append(node.val)
            s.extend(node.children)
        ans.reverse()
        return ans


solution = Solution2()
root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
assert [5,6,3,2,4,1] == solution.postorder(root)
