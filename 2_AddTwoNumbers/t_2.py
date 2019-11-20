# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        dummy = pre = ListNode(0)
        carry = 0

        while p1 and p2:
            val = p1.val + p2.val + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            pre.next = ListNode(val)
            p1, p2, pre = p1.next, p2.next, pre.next

        p = p1 or p2
        while p:
            val = p.val + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            pre.next = ListNode(val)
            p, pre = p.next, pre.next

        if carry:
            pre.next = ListNode(carry)

        return dummy.next
