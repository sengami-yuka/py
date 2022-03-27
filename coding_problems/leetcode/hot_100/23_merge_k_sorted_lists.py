# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.next
        return str(a)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def __lt__(this, other):
            return this.val < other.val
        ListNode.__lt__ = __lt__
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, lst)
        head = ListNode()
        cur = head
        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, cur.next)
        return head.next


solution = Solution()
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6)),
]
node = solution.mergeKLists(lists)
print(node)

lists = [
]
node = solution.mergeKLists(lists)
print(node)

lists = [
    None
]
node = solution.mergeKLists(lists)
print(node)
