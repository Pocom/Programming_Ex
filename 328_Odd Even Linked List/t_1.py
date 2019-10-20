# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        o = head
        s = e = head.next
        while o and e and e.next:
            o.next, e.next = e.next, e.next.next
            o, e = o.next, e.next
        return head