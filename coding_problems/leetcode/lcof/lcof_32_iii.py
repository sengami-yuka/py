# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = collections.deque()
        if root:
            q.append(root)
        while q:
            L = len(q)
            row = [0] * L
            it = range(L) if len(ans) % 2 == 0 else reversed(range(L))
            for i in it:
                node = q.popleft()
                row[i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row)
        return ans


solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
ans = solution.levelOrder(root)
assert ans == [
  [3],
  [20,9],
  [15,7]
]
