# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        root.val = 1
        q = [root]
        while q:
            node = q.pop()
            val = node.val
            depth = max(depth, val)
            if node.left:
                node.left.val = val + 1
                q.append(node.left)
            if node.right:
                node.right.val = val + 1
                q.append(node.right)
        return depth


solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ans = solution.maxDepth(root)
print(ans)
