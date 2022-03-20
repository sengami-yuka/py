# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(a, b):
            if not b:
                return True
            if not a or a.val != b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)
        if not A or not B:
            return False
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


solution = Solution()
A = TreeNode(1, TreeNode(2), TreeNode(3))
B = TreeNode(3, TreeNode(1))
assert not solution.isSubStructure(A, B)

A = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(4))
B = TreeNode(4, TreeNode(1))
assert solution.isSubStructure(A, B)

# [4,2,3,4,5,6,7,8,9]
# [4,8,9]
A = TreeNode(4, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
B = TreeNode(4, TreeNode(8), TreeNode(9))
assert solution.isSubStructure(A, B)

# [1,0,1,-4,-3]
# [1,-4]
A = TreeNode(1, TreeNode(0, TreeNode(-4), TreeNode(-3)), TreeNode(1))
B = TreeNode(1, TreeNode(-4))
assert not solution.isSubStructure(A, B)
