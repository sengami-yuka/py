# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node, depth):
            nonlocal max_depth, ans
            if node:
                dfs(node.left, depth + 1)
                if depth > max_depth:
                    max_depth = depth
                    ans = node.val
                dfs(node.right, depth + 1)
        max_depth = -1
        ans = 0
        dfs(root, 0)
        return ans


solution = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
ans = solution.findBottomLeftValue(root)
assert 1 == ans, ans

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
ans = solution.findBottomLeftValue(root)
assert 7 == ans, ans
