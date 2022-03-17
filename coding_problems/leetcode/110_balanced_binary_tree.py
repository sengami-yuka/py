# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            assert abs(left - right) <= 1
            return max(left, right) + 1
        try:
            dfs(root)
        except AssertionError:
            return False
        return True


solution = Solution()
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
ans = solution.isBalanced(root)
assert not ans

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ans = solution.isBalanced(root)
assert ans

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
ans = solution.isBalanced(root)
assert not ans

ans = solution.isBalanced(None)
assert ans
