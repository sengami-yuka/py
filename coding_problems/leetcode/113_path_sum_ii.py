from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(node, val):
            if node:
                val += node.val
                path.append(node.val)
                if not node.left and not node.right and val == target:
                    ans.append(path[:])
                else:
                    left = dfs(node.left, val)
                    right = dfs(node.right, val)
                path.pop()
        path = []
        ans = []
        dfs(root, 0)
        return ans


solution = Solution()
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
ans = solution.pathSum(root, 22)
assert ans == [[5,4,11,2],[5,8,4,5]], ans

root = TreeNode(1, TreeNode(2), TreeNode(3))
ans = solution.pathSum(root, 5)
assert ans == [], ans

root = TreeNode(1, TreeNode(2))
ans = solution.pathSum(root, 0)
assert ans == [], ans

root = TreeNode(0)
ans = solution.pathSum(root, 0)
assert ans == [[0]], ans
