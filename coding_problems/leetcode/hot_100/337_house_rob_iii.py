# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            l1, l2 = dfs(node.left)
            # print(l1, l2)
            r1, r2 = dfs(node.right)
            return node.val + l2 + r2, max(l1, l2) + max(r1, r2)
        return max(dfs(root))


solution = Solution()
root = TreeNode(3, TreeNode(2, TreeNode(3)), TreeNode(3, TreeNode(1)))
assert solution.rob(root) == 7

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, TreeNode(1)))
assert solution.rob(root) == 9


root = TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3))))
ans = solution.rob(root)
assert ans == 7, ans
