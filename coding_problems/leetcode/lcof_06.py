# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x, other=None):
        self.val = x
        self.next = other


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans[::-1]


solution = Solution()
head = ListNode(1, ListNode(3, ListNode(2)))
assert [2,3,1] == solution.reversePrint(head)
