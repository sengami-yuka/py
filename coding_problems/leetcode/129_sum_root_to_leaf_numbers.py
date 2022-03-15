# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, val):
            nonlocal ans
            val = 10 * val + node.val
            if not node.left and not node.right:
                ans += val
            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)
        ans = 0
        dfs(root, 0)
        return ans


class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, val):
            if not node:
                return 0
            val = 10 * val + node.val
            if not node.left and not node.right:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)


solution = Solution2()
root = TreeNode(1, TreeNode(2), TreeNode(3))
assert 25 == solution.sumNumbers(root)

root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
assert 1026 == solution.sumNumbers(root)
