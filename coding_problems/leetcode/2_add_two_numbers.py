# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = []
        it = self
        while it:
            res.append(str(it.val))
            it = it.next
        return '[' + ','.join(res) + ']'


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode()
        cur = ans
        carry = 0
        while carry or l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0
            cur.next = ListNode(s)
            cur = cur.next

        return ans.next


s = Solution()
a = ListNode(2, ListNode(4, ListNode(3)))
b = ListNode(5, ListNode(6, ListNode(4)))
print(s.addTwoNumbers(a, b))

a = ListNode(0)
b = ListNode(0)
print(s.addTwoNumbers(a, b))

a = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
b = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(s.addTwoNumbers(a, b))
