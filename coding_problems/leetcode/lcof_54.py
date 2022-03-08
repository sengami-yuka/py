# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.left)
        self.k = k
        inorder(root)
        return self.res


solution = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
assert 4 == solution.kthLargest(root, 1)
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
assert 4 == solution.kthLargest(root, 3)

