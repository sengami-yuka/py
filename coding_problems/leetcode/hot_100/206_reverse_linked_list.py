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
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        cur = head
        while cur:
            last, cur.next, cur = cur, last, cur.next
        return last


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new


solution = Solution2()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ans = solution.reverseList(head)
print(ans)

head = ListNode(1, ListNode(2))
ans = solution.reverseList(head)
print(ans)

head = None
ans = solution.reverseList(head)
print(ans)
