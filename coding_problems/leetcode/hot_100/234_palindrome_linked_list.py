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
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        cur = head
        while cur:
            a.append(cur.val)
            cur = cur.next
        for i in range(len(a) // 2):
            if a[i] != a[-i - 1]:
                return False
        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        last = prelast = None
        while fast and fast.next:
            fast = fast.next.next
            last = slow
            slow = slow.next
            last.next = prelast
            prelast = last
        if fast:
            slow = slow.next
        while slow:
            if slow.val != last.val:
                return False
            slow = slow.next
            last = last.next
        return True


solution = Solution2()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
ans = solution.isPalindrome(head)
assert ans

head = ListNode(1, ListNode(2))
ans = solution.isPalindrome(head)
assert not ans

head = ListNode(1, ListNode(2, ListNode(1)))
ans = solution.isPalindrome(head)
assert ans

head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
ans = solution.isPalindrome(head)
assert ans
