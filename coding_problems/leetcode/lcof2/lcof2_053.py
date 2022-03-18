# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(%d)' % self.val


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        ans = None
        while root:
            if root.val > p.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


solution = Solution()
p = TreeNode(1)
root = TreeNode(2, p, TreeNode(3))
ans = solution.inorderSuccessor(root, p)
assert ans == root, ans

p = TreeNode(6)
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), p)
ans = solution.inorderSuccessor(root, p)
assert ans is None, ans

out = TreeNode(3)
root = TreeNode(2, None, out)
ans = solution.inorderSuccessor(root, root)
assert ans == out, ans
