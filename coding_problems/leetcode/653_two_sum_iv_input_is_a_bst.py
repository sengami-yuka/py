# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node):
            if not node:
                return False
            if node.val in d:
                return True
            d.add(k - node.val)
            return dfs(node.left) or dfs(node.right)
        d = set()
        return dfs(root)


class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        stack = [root]
        d = set()
        while stack:
            node = stack.pop()
            if node.val in d:
                return True
            d.add(k - node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


class Solution3:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left, right = root, root
        leftStk, rightStk = [left], [right]
        while left.left:
            left = left.left
            leftStk.append(left)
        while right.right:
            right = right.right
            rightStk.append(right)
        while left != right:
            sum = left.val + right.val
            if sum == k:
                return True
            if sum < k:
                left = leftStk.pop()
                node = left.right
                while node:
                    leftStk.append(node)
                    node = node.left
            else:
                right = rightStk.pop()
                node = right.left
                while node:
                    rightStk.append(node)
                    node = node.right
        return False


solution = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
assert solution.findTarget(root, 9)
assert not solution.findTarget(root, 28)
