# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def dfs(node):
            if node:
                dfs(node.left)
                a.append(node.val)
                dfs(node.right)
        a = []
        dfs(self)
        return str(a)


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        self.val = 0
        dfs(root)
        return root


class Solution2:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node: TreeNode) -> TreeNode:
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ

        total = 0
        node = root

        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = getSuccessor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root


solution = Solution2()
root = TreeNode(4, TreeNode(1, TreeNode(0, 0, 0), TreeNode(2, 0, TreeNode(3, 0, 0))),
                TreeNode(6, TreeNode(5, 0, 0), TreeNode(7, 0, TreeNode(8, 0, 0))))
print(root)
solution.convertBST(root)
print(root)
