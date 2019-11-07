# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head.next or m == n: return head

        h = l1 = l2 = start = head
        M = m
        if m > 1:
            while m > 1:
                m -= 1
                n -= 1
                if m == 1:
                    start = h
                    l1 = l2 = h.next
                h = h.next
        rev, p = None, l1
        for _ in range(n):
            rev, rev.next, l1 = l1, rev, l1.next

        if M > 1:
            start.next, l2.next = rev, l1
        else:
            l2.next = l1
            head = rev
        return head
