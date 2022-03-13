# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


solution = Solution()
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, p, q)
ans = solution.lowestCommonAncestor(root, p, q)
assert ans == root

q = TreeNode(4)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
root = TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8)))
ans = solution.lowestCommonAncestor(root, p, q)
assert ans == p
