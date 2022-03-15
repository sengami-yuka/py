# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            nonlocal pre
            if node:
                dfs(node.left)
                assert pre < node.val
                pre = node.val
                dfs(node.right)
        pre = float('-inf')
        try:
            dfs(root)
        except AssertionError:
            return False
        return True


solution = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
assert solution.isValidBST(root)

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
assert not solution.isValidBST(root)
