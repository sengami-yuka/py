# Definition for singly-linked list.
class ListNode:
    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.next
        return str(a)

    def __init__(self, x, other=None):
        self.val = x
        self.next = other


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


solution = Solution()
head = ListNode('a', ListNode('b', ListNode('c', ListNode('d', ListNode('e', ListNode('f'))))))
print(head)
node = head.next.next.next.next
solution.deleteNode(node)
print(head)
