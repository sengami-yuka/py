# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        LA = 0
        while cur:
            LA += 1
            cur = cur.next
        cur = headB
        LB = 0
        while cur:
            LB += 1
            cur = cur.next
        a = headA
        b = headB
        if LA > LB:
            for _ in range(LA - LB):
                a = a.next
        elif LA < LB:
            for _ in range(LB - LA):
                b = b.next
        while a:
            if a == b:
                return a
            a = a.next
            b = b.next


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        cur = headA
        while cur:
            s.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in s:
                return cur
            cur = cur.next


class Solution3:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA


solution = Solution3()
c = ListNode(8, ListNode(4, ListNode(5)))
a = ListNode(4, ListNode(1, c))
b = ListNode(5, ListNode(0, ListNode(1, c)))
assert c == solution.getIntersectionNode(a, b)
