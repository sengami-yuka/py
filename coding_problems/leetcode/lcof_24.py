# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        cur = head
        while cur:
            last, cur.next, cur = cur, last, cur.next
        return last
