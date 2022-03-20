# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            ans = max(ans, left + right + node.val)
            return node.val + max(left, right)
        ans = float('-inf')
        dfs(root)
        return ans


solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
ans = solution.maxPathSum(root)
assert ans == 6, ans

root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ans = solution.maxPathSum(root)
assert ans == 42, ans
