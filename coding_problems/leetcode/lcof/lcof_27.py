# Definition for a binary tree node.
import collections


class TreeNode:
    def __repr__(self):
        a = []
        q = collections.deque([self])
        while q:
            node = q.popleft()
            if node:
                a.append(node.val)
                if node.left or node.right:
                    q.append(node.left)
                    q.append(node.right)
            else:
                a.append(None)
        return str(a)

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left, root.right = right, left
        return root


solution = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(root)
ans = solution.mirrorTree(root)
print(ans)

