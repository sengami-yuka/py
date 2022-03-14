# Definition for a binary tree node.
from typing import List
import collections


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        q = collections.deque()
        q.append(self)
        a = []
        while q:
            node = q.popleft()
            if node:
                a.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                a.append(None)
        while a[-1] is None:
            a.pop()
        return str(a)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pleft, pright, ileft):
            if pleft >= pright:
                return
            val = preorder[pleft]
            node = TreeNode(val)
            root_idx = d[val]
            left_size = root_idx - ileft
            node.left = helper(pleft + 1, pleft + left_size + 1, ileft)
            node.right = helper(pleft + left_size + 1, pright, root_idx + 1)
            return node
        d = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(preorder), 0)


solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = solution.buildTree(preorder, inorder)
assert str([3,9,20,None,None,15,7]) == str(root), root

preorder = [-1]
inorder = [-1]
root = solution.buildTree(preorder, inorder)
assert str([-1]) == str(root)
