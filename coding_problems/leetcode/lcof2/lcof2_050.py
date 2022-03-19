# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node):
            if not node:
                return 0
            a.append(node.val)
            s = 0
            ret = 0
            for i in reversed(range(len(a))):
                s += a[i]
                if s == targetSum:
                    ret += 1
            ret += dfs(node.left)
            ret += dfs(node.right)
            a.pop()
            return ret

        a = []
        return dfs(root)


class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            curr += node.val
            ret = prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            prefix[curr] -= 1
            return ret
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)


solution = Solution2()
root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
ans = solution.pathSum(root, 8)
assert 3 == ans, ans

# [5,4,8,11,null,13,4,7,2,null,null,5,1]
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
# print(root)
ans = solution.pathSum(root, 22)
assert 3 == ans, ans

# [1, 2]
root = TreeNode(1, TreeNode(2))
# print(root)
ans = solution.pathSum(root, 2)
assert 1 == ans, ans

# [1]
root = TreeNode(1)
# print(root)
ans = solution.pathSum(root, 1)
assert 1 == ans, ans
ans = solution.pathSum(root, 0)
assert 0 == ans, ans
