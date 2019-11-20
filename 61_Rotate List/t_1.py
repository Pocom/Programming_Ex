# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not k or not head.next: return head

        p, cnt = head, 0
        while p:
            cnt += 1
            p = p.next

        k %= cnt
        if k == 0: return head

        def reverse(head):
            p, rev = head, None
            while p:
                rev, rev.next, p = p, rev, p.next
            return rev

        rev = reverse(head)
        head.next = rev

        while k > 1:
            k -= 1
            rev = rev.next

        ptr = rev.next
        rev.next = None

        return reverse(ptr)
