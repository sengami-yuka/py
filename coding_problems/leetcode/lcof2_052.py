# Definition for a binary tree node.
class TreeNode:
    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.right
        return str(a)

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node):
        if node.left:
            left_head, left_tail = self.helper(node.left)
            left_tail.right = node
        else:
            left_head = node
        if node.right:
            node.right, right_tail = self.helper(node.right)
        else:
            right_tail = node
        node.left = None
        return left_head, right_tail

    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]


class Solution2:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.cur.right = node
        node.left = None
        self.cur = node
        self.inorder(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        self.cur = dummy
        self.inorder(root)
        return dummy.right


solution = Solution()
# root = TreeNode(5, TreeNode(1), TreeNode(7))
# ans = solution.increasingBST(root)
# print(ans)

root = TreeNode(3, TreeNode(2, TreeNode(1)))
root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
ans = solution.increasingBST(root)
print(ans)
