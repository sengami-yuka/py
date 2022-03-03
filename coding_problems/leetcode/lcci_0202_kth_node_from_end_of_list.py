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
    def kthToLast(self, head: ListNode, k: int) -> int:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        cur = head
        for i in range(length - k):
            cur = cur.next
        return cur.val

    def kthToLast2(self, head: ListNode, k: int) -> int:
        i = head
        j = head
        for _ in range(k):
            j = j.next
        while j:
            i = i.next
            j = j.next
        return i.val


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(head)
assert 4 == solution.kthToLast(head, 2)
assert 4 == solution.kthToLast2(head, 2)
