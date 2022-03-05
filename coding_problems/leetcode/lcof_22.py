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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i = head
        j = head
        for _ in range(k):
            j = j.next
        while j:
            i = i.next
            j = j.next
        return i


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(solution.getKthFromEnd(head, 2))
