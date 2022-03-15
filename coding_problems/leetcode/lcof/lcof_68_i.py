# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        while 1:
            if p.val < ans.val and q.val < ans.val:
                ans = ans.left
            elif p.val > ans.val and q.val > ans.val:
                ans = ans.right
            else:
                break
        return ans
