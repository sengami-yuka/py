# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        depth(root)
        return self.ans


solution = Solution()

head = TreeNode(1)
assert 0 == solution.diameterOfBinaryTree(head)

head = TreeNode(1, TreeNode(1))
assert 1 == solution.diameterOfBinaryTree(head)

head = TreeNode(1, TreeNode(1), TreeNode(1))
assert 2 == solution.diameterOfBinaryTree(head)

head = TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1))
assert 3 == solution.diameterOfBinaryTree(head)

head = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
assert 3 == solution.diameterOfBinaryTree(head)

head = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
assert 3 == solution.diameterOfBinaryTree(head)
