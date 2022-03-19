import collections
import json
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                a.append(node.val)

        a = []
        dfs(self)
        return json.dumps(a, separators=(',', ':'))


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        left = []
        right = []
        for i in range(len(postorder) - 1):
            if postorder[i] < root:
                left.append(postorder[i])
                if right:
                    return False
            else:
                right.append(postorder[i])
        return self.verifyPostorder(left) and self.verifyPostorder(right)


class Solution2:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for val in reversed(postorder):
            if val > root:
                return False
            while stack and val < stack[-1]:
                root = stack.pop()
            stack.append(val)
        return True


solution = Solution2()
ans = solution.verifyPostorder([1,6,3,2,5])
assert not ans
ans = solution.verifyPostorder([1,3,2,6,5])
assert ans
