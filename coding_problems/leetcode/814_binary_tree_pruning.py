# Definition for a binary tree node.
import collections
import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        q = collections.deque()
        q.append(self)
        a = []
        while q:
            node = q.popleft()
            if node:
                a.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                a.append(None)
        while a[-1] is None:
            a.pop()
        return json.dumps(a, separators=(',', ':'))


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return
        return root


solution = Solution()
root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
print(root)
ans = solution.pruneTree(root)
print(ans)

root = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
print(root)
ans = solution.pruneTree(root)
print(ans)

root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0)), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
print(root)
ans = solution.pruneTree(root)
print(ans)
