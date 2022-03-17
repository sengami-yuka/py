# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            ans = max(ans, left + right + node.val)
            return max(left, right) + node.val
        ans = float('-inf')
        dfs(root)
        return ans


solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
assert 6 == solution.maxPathSum(root)

root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert 42 == solution.maxPathSum(root)

root = TreeNode(2, TreeNode(-1))
assert 2 == solution.maxPathSum(root)

root = TreeNode(1, TreeNode(-1), TreeNode(3))
assert 4 == solution.maxPathSum(root)

# [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
root = TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6, TreeNode(-6)), TreeNode(-6)))))
ans = solution.maxPathSum(root)
assert 16 == ans, ans
