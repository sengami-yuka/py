from typing import List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        ans = []
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if len(ans) <= level:
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return ans


class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        ans = []
        q.append(root)
        while q:
            n = len(q)
            row = []
            for _ in range(n):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row)
        return ans


solution = Solution2()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert [[3],[9,20],[15,7]] == solution.levelOrder(root)

root = TreeNode(1)
assert [[1]] == solution.levelOrder(root)
