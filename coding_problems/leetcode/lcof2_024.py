# Definition for singly-linked list.
class ListNode:
    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.next
        return str(a)

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, last = head, None
        while cur:
            cur, last, last.next = cur.next, cur, last
        return last


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ans = solution.reverseList(head)
print(ans)
