# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left = [root.left]
        right = [root.right]
        while left:
            i = left.pop()
            j = right.pop()
            if not i and not j:
                continue
            if not i or not j or i.val != j.val:
                return False
            left.append(i.left)
            right.append(j.right)
            left.append(i.right)
            right.append(j.left)
        return True


class Solution2:
    def s(self, left, right):
        if not left and not right:
            return True
        return left is not None and right is not None and left.val == right.val and self.s(left.left, right.right) and self.s(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.s(root, root)


solution = Solution2()
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

ans = solution.isSymmetric(root)
print(ans)
