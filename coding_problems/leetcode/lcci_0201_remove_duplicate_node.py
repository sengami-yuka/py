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
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        cur = head
        d = set()
        while cur:
            if cur.val in d:
                last.next = cur.next
            else:
                d.add(cur.val)
                last = cur
            cur = cur.next
        return head

    # def removeDuplicateNodes2(self, head: ListNode) -> ListNode:
    #     i = head
    #     while i:
    #         j = i
    #         while j.next:
    #             if j.next.val == i.val:
    #                 j.next = j.next.next
    #             else:
    #                 j = j.next
    #         i = i.next
    #     return head


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
# [1, 2, 3, 3, 2, 1]
print(head)
solution.removeDuplicateNodes(head)
print(head)
