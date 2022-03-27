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

    def __gt__(self, other):
        return self.val > other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i))
        head = ListNode()
        cur = head
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            lists[i] = lists[i].next
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val, i))
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
