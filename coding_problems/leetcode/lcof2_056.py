# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(node):
            if not node:
                return False
            if node.val in s:
                return True
            s.add(k - node.val)
            return dfs(node.left) or dfs(node.right)
        s = set()
        return dfs(root)


solution = Solution()
root = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
assert solution.findTarget(root, 12)
root = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
assert not solution.findTarget(root, 22)
