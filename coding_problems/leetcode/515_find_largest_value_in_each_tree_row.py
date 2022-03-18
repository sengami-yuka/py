# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth >= len(ans):
                    ans.append(node.val)
                ans[depth] = max(node.val, ans[depth])
                depth += 1
                dfs(node.left, depth)
                dfs(node.right, depth)
        ans = []
        dfs(root, 0)
        return ans


class Solution2:
    def largestValues(self, root):
        ans, q = [], collections.deque()
        if root:
            q.append(root)
        while q:
            num = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                num = max(num, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(num)
        return ans


solution = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
assert [1,3,9] == solution.largestValues(root)
root = TreeNode(1, TreeNode(2), TreeNode(3))
assert [1,3] == solution.largestValues(root)
root = TreeNode(1)
assert [1] == solution.largestValues(root)
root = TreeNode(1, None, TreeNode(2))
assert [1,2] == solution.largestValues(root)
assert [] == solution.largestValues(None)
